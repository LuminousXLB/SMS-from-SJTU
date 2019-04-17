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
        err_msg = manager.post_credentials(
            request.user, request.passwd, request.captcha)
        return proto.GeneralResponse(success=not err_msg, message=err_msg)


class SmsService(proto.SmsServicer):
    table = {
        '12345': '13512345678',
        '12346': '13612345678',
        '12347': '13898130558'
    }

    def SendSMS(self, request_iterator, context):
        for request in request_iterator:
            print('send message: ', request.phone_number, request.content)
        return proto.SendMessageResponse(success=True, receiveid='12345')

    def ReceiveMessage(self, request, context):

        receive_id = request.receive_id
        print(time.ctime(), 'receive message: ', request.receive_id)
        phone_number = self.table.get(request.receive_id)

        while phone_number:
            yield proto.ReceiveMessageResponse(
                receive_id=receive_id,
                send_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                phone_number=phone_number,
                content='ok'
            )
            receive_id = str(int(receive_id) + 1)
            print(time.ctime(), 'receive message: ', receive_id)
            phone_number = self.table.get(receive_id)


# class SmsService(proto.SmsServicer):
#     def SendSMS(self, request_iterator, context):
#         for request in request_iterator:
#             manager.send_sms(request.phone_number, request.content)
#         receive_id = manager.get_current_id()
#         return proto.SendMessageResponse(success=True, receiveid=receive_id)
#
#     def ReceiveMessage(self, request, context):
#         print('receive message: ', request.receive_id)
#
#         receive_id = request.receive_id
#         send_time, phone_number, content = manager.receive_sms(receive_id)
#
#         while phone_number:
#             yield proto.ReceiveMessageResponse(
#                 receive_id=receive_id,
#                 send_time=send_time,
#                 phone_number=phone_number,
#                 content=content
#             )
#             receive_id = str(int(receive_id) + 1)
#             send_time, phone_number, content = manager.receive_sms(receive_id)


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
