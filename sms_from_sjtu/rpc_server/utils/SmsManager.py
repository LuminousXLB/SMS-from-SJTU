from utils.JAccountLoginManager import JAccountLoginManager, take_qs
from utils.logger import logger_factory
from bs4 import BeautifulSoup
import datetime

logger = logger_factory()


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

    def send_sms(self, phone_number, content):
        content_length = len(content) + 1
        message_number = 0
        while content_length > 0:
            message_number += 1
            content_length -= 60

        form = {
            'phonecode': phone_number,
            'sendtotal': '1',
            'content': content,
            'charsNum': str(len(content)),
            'msgNum': str(message_number),
            'istime': '0',
            'senddate': '%s 0:0:00' % datetime.date.today().strftime('%Y/%m/%d'),
            'sdate': datetime.date.today().strftime('%Y/%m/%d'),
            'hour': '0',
            'minute': '0',
            'btn/': '发 送 短 信',
            'phonecodesel': '',
            'userName': '',
            'ids': ''
        }

        self.post('send', 'http://sms.sjtu.edu.cn/SMS/sms/sendBoxAdd.do?method.save', form)

    def get_current_id(self):
        rsp = self.get('get_id', 'http://sms.sjtu.edu.cn/SMS/sms/recBoxQuery.do?method.query')
        soup = BeautifulSoup(rsp.content, 'html.parser')
        table_list = soup.find('table', id='tableList')
        href = table_list.find_all('a')[0].get('href')
        return href.split('=')[-1]

    def receive_sms(self, receive_id):
        url = 'http://sms.sjtu.edu.cn/SMS/sms/recBoxView.do?method=view&receiveid={}'.format(receive_id)
        rsp = self.get('receive', url)
        soup = BeautifulSoup(rsp.content, 'html.parser')

        lst = soup.find(id='tableInput').findAll('tr')

        phone_number = lst[1].findAll('td')[1].text.replace('&nbsp', '').strip()
        send_time = lst[2].findAll('td')[1].text.replace('&nbsp', '').strip()
        content = lst[3].findAll('td')[1].text.replace('&nbsp', '').strip()

        logger.info('[%s] %s > %s' % (send_time, phone_number, content))

        return send_time, phone_number, content

    # def convert_lessons_to_ics(self, firstday):
    #     url = 'http://electsys.sjtu.edu.cn/edu/newsBoard/newsInside.aspx'
    #     rsp = self.session.get(url)
    #     soup = BeautifulSoup(rsp.text, 'html.parser')
    #     lesson_list = extract_lessons_from_soup(soup)
    #     return lesson_list
