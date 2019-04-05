from utils import JAccountLoginManager


class ElectSysManager(JAccountLoginManager):
    def get_login_url(self):
        return 'http://electsys.sjtu.edu.cn/edu/login.aspx'

    def check_login_result(self, rsp):
        ret = super().check_login_result(rsp)
        if ret:
            return ret
        success_url = 'http://electsys.sjtu.edu.cn/edu/student/sdtMain.aspx'
        if rsp.request.url == success_url:
            return ''
        if 'electsys.sjtu.edu.cn' in rsp.request.url:
            qs = take_qs(rsp.request.url)
            msg = qs.get('message', [''])[0]
            if msg:
                return 'ElectSys says: ' + msg
        return '未知错误'

    def convert_lessons_to_ics(self, firstday):
        url = 'http://electsys.sjtu.edu.cn/edu/newsBoard/newsInside.aspx'
        rsp = self.session.get(url)
        soup = BeautifulSoup(rsp.text, 'html.parser')
        lesson_list = extract_lessons_from_soup(soup)
        return lesson_list
        # return generate_ics(lesson_list, firstday)
