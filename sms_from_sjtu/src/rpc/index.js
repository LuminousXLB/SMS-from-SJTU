import { JaccountServiceClient } from './proto/jaccount_grpc_pb'
import { CaptchaNonce, LoginForm } from './proto/jaccount_pb'

import grpc from 'grpc'

const client = new JaccountServiceClient(
  'localhost:50051',
  grpc.credentials.createInsecure()
)

export function getCaptcha() {
  return new Promise((resolve, reject) => {
    let request = new CaptchaNonce()
    request.setNonce(`${new Date().getTime()}`)

    client.getCaptcha(request, function(err, response) {
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
    client.submitCredentials(request, function(err, response) {
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
