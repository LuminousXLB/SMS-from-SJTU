// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var sms_pb = require('./sms_pb.js');
var jaccount_pb = require('./jaccount_pb.js');

function serialize_GeneralResponse(arg) {
  if (!(arg instanceof jaccount_pb.GeneralResponse)) {
    throw new Error('Expected argument of type GeneralResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_GeneralResponse(buffer_arg) {
  return jaccount_pb.GeneralResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_MessagesInfos(arg) {
  if (!(arg instanceof sms_pb.MessagesInfos)) {
    throw new Error('Expected argument of type MessagesInfos');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_MessagesInfos(buffer_arg) {
  return sms_pb.MessagesInfos.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_MessagesPlain(arg) {
  if (!(arg instanceof sms_pb.MessagesPlain)) {
    throw new Error('Expected argument of type MessagesPlain');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_MessagesPlain(buffer_arg) {
  return sms_pb.MessagesPlain.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_PhoneNumbers(arg) {
  if (!(arg instanceof sms_pb.PhoneNumbers)) {
    throw new Error('Expected argument of type PhoneNumbers');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_PhoneNumbers(buffer_arg) {
  return sms_pb.PhoneNumbers.deserializeBinary(new Uint8Array(buffer_arg));
}


var SmsService = exports.SmsService = {
  sendPlainMessages: {
    path: '/Sms/SendPlainMessages',
    requestStream: false,
    responseStream: false,
    requestType: sms_pb.MessagesPlain,
    responseType: jaccount_pb.GeneralResponse,
    requestSerialize: serialize_MessagesPlain,
    requestDeserialize: deserialize_MessagesPlain,
    responseSerialize: serialize_GeneralResponse,
    responseDeserialize: deserialize_GeneralResponse,
  },
  sendInnovMessages: {
    path: '/Sms/SendInnovMessages',
    requestStream: false,
    responseStream: false,
    requestType: sms_pb.MessagesInfos,
    responseType: jaccount_pb.GeneralResponse,
    requestSerialize: serialize_MessagesInfos,
    requestDeserialize: deserialize_MessagesInfos,
    responseSerialize: serialize_GeneralResponse,
    responseDeserialize: deserialize_GeneralResponse,
  },
  receiveMessages: {
    path: '/Sms/ReceiveMessages',
    requestStream: false,
    responseStream: false,
    requestType: sms_pb.PhoneNumbers,
    responseType: sms_pb.MessagesInfos,
    requestSerialize: serialize_PhoneNumbers,
    requestDeserialize: deserialize_PhoneNumbers,
    responseSerialize: serialize_MessagesInfos,
    responseDeserialize: deserialize_MessagesInfos,
  },
};

exports.SmsClient = grpc.makeGenericClientConstructor(SmsService);
