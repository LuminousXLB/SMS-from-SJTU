from utils import SmsManager
import proto
import time
import grpc
from concurrent import futures

manager = SmsManager()


class JaccountServiceService(proto.JaccountServiceServicer):

    def GetCaptcha(self, request: proto.CaptchaNonce, context) -> proto.CaptchaImage:
        content_type, img_blob = manager.get_captcha(request.nonce)
        return proto.CaptchaImage(content_type=content_type, img_blob=img_blob)

    def SubmitCredentials(self, request: proto.SubmitCredentials, context) -> proto.GeneralResponse:
        err_msg = manager.post_credentials(request.user, request.passwd, request.captcha)
        return proto.GeneralResponse(success=not err_msg, message=err_msg)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto.add_JaccountServiceServicer_to_server(
        JaccountServiceService(),
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
