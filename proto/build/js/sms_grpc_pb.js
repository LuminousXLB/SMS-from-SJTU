// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var sms_pb = require('./sms_pb.js');

function serialize_ReceiveMessageRequest(arg) {
  if (!(arg instanceof sms_pb.ReceiveMessageRequest)) {
    throw new Error('Expected argument of type ReceiveMessageRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_ReceiveMessageRequest(buffer_arg) {
  return sms_pb.ReceiveMessageRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_ReceiveMessageResponse(arg) {
  if (!(arg instanceof sms_pb.ReceiveMessageResponse)) {
    throw new Error('Expected argument of type ReceiveMessageResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_ReceiveMessageResponse(buffer_arg) {
  return sms_pb.ReceiveMessageResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_SendMessageRequest(arg) {
  if (!(arg instanceof sms_pb.SendMessageRequest)) {
    throw new Error('Expected argument of type SendMessageRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_SendMessageRequest(buffer_arg) {
  return sms_pb.SendMessageRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_SendMessageResponse(arg) {
  if (!(arg instanceof sms_pb.SendMessageResponse)) {
    throw new Error('Expected argument of type SendMessageResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_SendMessageResponse(buffer_arg) {
  return sms_pb.SendMessageResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var SmsService = exports.SmsService = {
  sendSMS: {
    path: '/Sms/SendSMS',
    requestStream: true,
    responseStream: false,
    requestType: sms_pb.SendMessageRequest,
    responseType: sms_pb.SendMessageResponse,
    requestSerialize: serialize_SendMessageRequest,
    requestDeserialize: deserialize_SendMessageRequest,
    responseSerialize: serialize_SendMessageResponse,
    responseDeserialize: deserialize_SendMessageResponse,
  },
  receiveMessage: {
    path: '/Sms/ReceiveMessage',
    requestStream: false,
    responseStream: true,
    requestType: sms_pb.ReceiveMessageRequest,
    responseType: sms_pb.ReceiveMessageResponse,
    requestSerialize: serialize_ReceiveMessageRequest,
    requestDeserialize: deserialize_ReceiveMessageRequest,
    responseSerialize: serialize_ReceiveMessageResponse,
    responseDeserialize: deserialize_ReceiveMessageResponse,
  },
};

exports.SmsClient = grpc.makeGenericClientConstructor(SmsService);
