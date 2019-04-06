from utils.JAccountLoginManager import JAccountLoginManager
from utils.logger import get_logger

logger = get_logger()


class SmsManager(JAccountLoginManager):
    def get_login_url(self):
        return 'http://sms.sjtu.edu.cn/SMS'

    def check_login_result(self, rsp):
        ret = super().check_login_result(rsp)
        if ret:
            return ret
        success_url = 'http://sms.sjtu.edu.cn/SMS/pages/main.jsp'
        if rsp.request.url == success_url:
            return ''
        if 'sms.sjtu.edu.cn' in rsp.request.url:
            return '该账号可能未开通短信服务'
        return '未知错误'

    # def convert_lessons_to_ics(self, firstday):
    #     url = 'http://electsys.sjtu.edu.cn/edu/newsBoard/newsInside.aspx'
    #     rsp = self.session.get(url)
    #     soup = BeautifulSoup(rsp.text, 'html.parser')
    #     lesson_list = extract_lessons_from_soup(soup)
    #     return lesson_list
