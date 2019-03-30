# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import jaccount_pb2 as jaccount__pb2
import sms_pb2 as sms__pb2


class SmsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendPlainMessages = channel.unary_unary(
        '/Sms/SendPlainMessages',
        request_serializer=sms__pb2.MessagesPlain.SerializeToString,
        response_deserializer=jaccount__pb2.GeneralResponse.FromString,
        )
    self.SendInnovMessages = channel.unary_unary(
        '/Sms/SendInnovMessages',
        request_serializer=sms__pb2.MessagesInfos.SerializeToString,
        response_deserializer=jaccount__pb2.GeneralResponse.FromString,
        )
    self.ReceiveMessages = channel.unary_unary(
        '/Sms/ReceiveMessages',
        request_serializer=sms__pb2.PhoneNumbers.SerializeToString,
        response_deserializer=sms__pb2.MessagesInfos.FromString,
        )


class SmsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendPlainMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendInnovMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReceiveMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SmsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendPlainMessages': grpc.unary_unary_rpc_method_handler(
          servicer.SendPlainMessages,
          request_deserializer=sms__pb2.MessagesPlain.FromString,
          response_serializer=jaccount__pb2.GeneralResponse.SerializeToString,
      ),
      'SendInnovMessages': grpc.unary_unary_rpc_method_handler(
          servicer.SendInnovMessages,
          request_deserializer=sms__pb2.MessagesInfos.FromString,
          response_serializer=jaccount__pb2.GeneralResponse.SerializeToString,
      ),
      'ReceiveMessages': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiveMessages,
          request_deserializer=sms__pb2.PhoneNumbers.FromString,
          response_serializer=sms__pb2.MessagesInfos.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Sms', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
