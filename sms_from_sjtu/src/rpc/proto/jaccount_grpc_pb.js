// GENERATED CODE -- DO NOT EDIT!

'use strict'
var grpc = require('grpc')
var jaccount_pb = require('./jaccount_pb.js')

function serialize_CaptchaImage(arg) {
  if (!(arg instanceof jaccount_pb.CaptchaImage)) {
    throw new Error('Expected argument of type CaptchaImage')
  }
  return Buffer.from(arg.serializeBinary())
}

function deserialize_CaptchaImage(buffer_arg) {
  return jaccount_pb.CaptchaImage.deserializeBinary(new Uint8Array(buffer_arg))
}

function serialize_CaptchaNonce(arg) {
  if (!(arg instanceof jaccount_pb.CaptchaNonce)) {
    throw new Error('Expected argument of type CaptchaNonce')
  }
  return Buffer.from(arg.serializeBinary())
}

function deserialize_CaptchaNonce(buffer_arg) {
  return jaccount_pb.CaptchaNonce.deserializeBinary(new Uint8Array(buffer_arg))
}

function serialize_GeneralResponse(arg) {
  if (!(arg instanceof jaccount_pb.GeneralResponse)) {
    throw new Error('Expected argument of type GeneralResponse')
  }
  return Buffer.from(arg.serializeBinary())
}

function deserialize_GeneralResponse(buffer_arg) {
  return jaccount_pb.GeneralResponse.deserializeBinary(
    new Uint8Array(buffer_arg)
  )
}

function serialize_LoginForm(arg) {
  if (!(arg instanceof jaccount_pb.LoginForm)) {
    throw new Error('Expected argument of type LoginForm')
  }
  return Buffer.from(arg.serializeBinary())
}

function deserialize_LoginForm(buffer_arg) {
  return jaccount_pb.LoginForm.deserializeBinary(new Uint8Array(buffer_arg))
}

// var JaccountServiceService = (exports.JaccountServiceService = {
export var JaccountServiceService = {
  getCaptcha: {
    path: '/JaccountService/GetCaptcha',
    requestStream: false,
    responseStream: false,
    requestType: jaccount_pb.CaptchaNonce,
    responseType: jaccount_pb.CaptchaImage,
    requestSerialize: serialize_CaptchaNonce,
    requestDeserialize: deserialize_CaptchaNonce,
    responseSerialize: serialize_CaptchaImage,
    responseDeserialize: deserialize_CaptchaImage
  },
  submitCredentials: {
    path: '/JaccountService/SubmitCredentials',
    requestStream: false,
    responseStream: false,
    requestType: jaccount_pb.LoginForm,
    responseType: jaccount_pb.GeneralResponse,
    requestSerialize: serialize_LoginForm,
    requestDeserialize: deserialize_LoginForm,
    responseSerialize: serialize_GeneralResponse,
    responseDeserialize: deserialize_GeneralResponse
  }
}

export var JaccountServiceClient = grpc.makeGenericClientConstructor(
  JaccountServiceService
)

// exports.JaccountServiceClient = grpc.makeGenericClientConstructor(
//   JaccountServiceService
// )
