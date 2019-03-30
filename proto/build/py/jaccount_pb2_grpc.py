# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import jaccount_pb2 as jaccount__pb2


class JaccountServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCaptcha = channel.unary_unary(
        '/JaccountService/GetCaptcha',
        request_serializer=jaccount__pb2.CaptchaNonce.SerializeToString,
        response_deserializer=jaccount__pb2.CaptchaImage.FromString,
        )
    self.SubmitCredentials = channel.unary_unary(
        '/JaccountService/SubmitCredentials',
        request_serializer=jaccount__pb2.LoginForm.SerializeToString,
        response_deserializer=jaccount__pb2.GeneralResponse.FromString,
        )


class JaccountServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCaptcha(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitCredentials(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JaccountServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCaptcha': grpc.unary_unary_rpc_method_handler(
          servicer.GetCaptcha,
          request_deserializer=jaccount__pb2.CaptchaNonce.FromString,
          response_serializer=jaccount__pb2.CaptchaImage.SerializeToString,
      ),
      'SubmitCredentials': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitCredentials,
          request_deserializer=jaccount__pb2.LoginForm.FromString,
          response_serializer=jaccount__pb2.GeneralResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'JaccountService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
