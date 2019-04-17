import { JaccountServiceClient } from './proto/jaccount_grpc_pb'
import { CaptchaNonce, LoginForm } from './proto/jaccount_pb'
import { ReceiveMessageRequest, SendMessageRequest } from './proto/sms_pb'
import { SmsClient } from './proto/sms_grpc_pb'
import store from '@/store'

// import async from 'async'
import grpc from 'grpc'

const jacClient = new JaccountServiceClient(
  'localhost:50051',
  grpc.credentials.createInsecure()
)

const smsClient = new SmsClient(
  'localhost:50051',
  grpc.credentials.createInsecure()
)

export function getCaptcha() {
  return new Promise((resolve, reject) => {
    let request = new CaptchaNonce()
    request.setNonce(`${new Date().getTime()}`)

    jacClient.getCaptcha(request, function(err, response) {
      if (err) {
        reject(err)
      } else {
        resolve(
          `data:${response.getContentType()};base64,${response.getImgBlob_asB64()}`
        )
      }
    })
  })
}

export function submitCredentials({ username, password, captcha }) {
  return new Promise((resolve, reject) => {
    let request = new LoginForm()
    request.setUser(username)
    request.setPasswd(password)
    request.setCaptcha(captcha)
    jacClient.submitCredentials(request, function(err, response) {
      if (err) {
        reject(err)
      } else {
        const success = response.getSuccess()
        const message = response.getMessage()
        resolve({ success, message })
      }
    })
  })
}

export function sendPlainMessage(phones, message) {
  return new Promise((resolve, reject) => {
    var call = smsClient.sendSMS((error, response) => {
      if (error) {
        reject(error)
      } else {
        const success = response.getSuccess()
        const receiveid = response.getReceiveid()
        resolve({ success, receiveid })
      }
    })

    for (let phone of phones) {
      let request = new SendMessageRequest()
      request.setPhoneNumber(phone)
      request.setContent(message)
      call.write(request)
      console.log(request)
    }

    call.end()
  })
}

export function sendTemplateMessage(form) {
  return new Promise((resolve, reject) => {
    var call = smsClient.sendSMS((error, response) => {
      if (error) {
        reject(error)
      } else {
        const success = response.getSuccess()
        const receiveid = response.getReceiveid()
        resolve({ success, receiveid })
      }
    })

    for (let { phone, message } of form) {
      let request = new SendMessageRequest()
      request.setPhoneNumber(phone)
      request.setContent(message)
      call.write(request)
      console.log(request)
    }

    call.end()
  })
}

export function recieveMessage(receiveid) {
  return new Promise((resolve, reject) => {
    let request = new ReceiveMessageRequest()
    request.setReceiveId(receiveid)
    console.log(request)

    let call = smsClient.receiveMessage(request)

    call.on('data', function(response) {
      // console.log(response)
      const id = response.getReceiveId()
      const time = response.getSendTime()
      const phone = response.getPhoneNumber()
      const message = response.getContent()
      store.commit('reply', { id, time, phone, message })
    })
    call.on('end', function() {
      resolve()
    })
    call.on('error', function(e) {
      reject(e)
    })
  })
}
