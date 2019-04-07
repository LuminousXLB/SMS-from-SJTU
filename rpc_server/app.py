from utils import SmsManager
import proto
import time
import grpc
import datetime
from concurrent import futures

manager = SmsManager()


class JaccountService(proto.JaccountServiceServicer):

    def GetCaptcha(self, request: proto.CaptchaNonce, context) -> proto.CaptchaImage:
        content_type, img_blob = manager.get_captcha(request.nonce)
        return proto.CaptchaImage(content_type=content_type, img_blob=img_blob)

    def SubmitCredentials(self, request: proto.LoginForm, context) -> proto.GeneralResponse:
        err_msg = manager.post_credentials(request.user, request.passwd, request.captcha)
        return proto.GeneralResponse(success=not err_msg, message=err_msg)


class SmsService(proto.SmsServicer):
    def SendSMS(self, request_iterator, context):
        for request in request_iterator:
            # manager.send_sms(request.phone_number, request.content)
            print('send message: ', request.phone_number, request.content)
        # receive_id = manager.get_current_id()
        # return proto.SendMessageResponse(success=True, receiveid=receive_id)
        return proto.SendMessageResponse(success=True, receiveid='12345')

    def ReceiveMessage(self, request, context):
        # send_time, phone_number, content = manager.receive_sms(request.receive_id)
        print('receive message: ', request.receive_id)
        # return proto.ReceiveMessageResponse(send_time, phone_number, content)
        return proto.ReceiveMessageResponse(send_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                            phone_number='13998316872', content='ok')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto.add_JaccountServiceServicer_to_server(
        JaccountService(),
        server
    )
    proto.add_SmsServicer_to_server(
        SmsService(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
