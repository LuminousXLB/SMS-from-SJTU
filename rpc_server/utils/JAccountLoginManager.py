from abc import ABCMeta, abstractmethod
from functools import wraps
from random import random
from urllib import parse
from bs4 import BeautifulSoup
import requests
from utils.logger import logger_factory

logger = logger_factory()


def with_max_retries(count):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                try:
                    ret = func(*args, **kwargs)
                except Exception as e:
                    logger.info('try %s: %r failed with %r', i, func, e)
                    if i == count - 1:
                        raise e
                else:
                    return ret

        return wrapper

    return real_decorator


def take_qs(url):
    return parse.parse_qs(parse.urlsplit(url).query)


def session_factory(ua=None):
    chrome = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    session = requests.Session()
    session.headers['User-Agent'] = ua or chrome
    return session


class JAccountLoginManager(metaclass=ABCMeta):
    def __init__(self, session=None):
        self.session = session or session_factory()
        self.variables = self._fetch_variables()

    def new_session(self, ua=None):
        self.session = session_factory(ua)
        self.variables = self._fetch_variables()

    @abstractmethod
    def get_login_url(self) -> str:
        pass

    @abstractmethod
    def check_login_result(self, rsp) -> 'error message':
        if 'jaccount.sjtu.edu.cn' in rsp.url:
            qs = take_qs(rsp.url)
            err = qs.get('err', [''])[0]
            if err == '0':
                return '请正确填写你的用户名和密码，注意：密码是区分大小写的'
            elif err == '1':
                return '请正确填写验证码'
            elif err == '2':
                return '服务器故障，请稍后再试'
            elif err == '3':
                return '委托代理的帐户不存在, 请重新选择'
            elif err == '4':
                return '委托代理的帐户已过期, 请重新选择'
            elif err == '5':
                return '当前的委托代理已失效, 请重新选择'
            else:
                return '未知登录错误'
        return ''

    @with_max_retries(3)
    def get_captcha(self, nonce=None) -> ('content type', 'image blob'):
        captcha_url = 'https://jaccount.sjtu.edu.cn/jaccount/captcha?uuid={uuid}&t={t}'.format(
            uuid=self.variables['uuid'],
            t=nonce or self._get_random()
        )
        rsp = self._get('captcha', captcha_url)
        return rsp.headers['Content-Type'], rsp.content

    @with_max_retries(3)
    def post_credentials(self, user, password, captcha) -> 'error message':
        payload = self.variables.copy()
        payload['user'] = user
        payload['pass'] = password
        payload['captcha'] = captcha

        rsp = self._post('login', 'https://jaccount.sjtu.edu.cn/jaccount/ulogin', payload)
        return self.check_login_result(rsp)

    @with_max_retries(3)
    def _fetch_variables(self):
        rsp = self._get('login page', self.get_login_url())
        self.login_ret_url = rsp.url
        form = BeautifulSoup(rsp.text, 'html.parser').find(id='form-input')
        return {
            it.attrs['name']: it.attrs.get('value', '')
            for it in form.find_all('input', attrs={'name': True})
        }

    def _get(self, name, url):
        rsp = self.session.get(url)
        self._log(name, rsp)
        return rsp

    def _post(self, name, url, data):
        rsp = self.session.post(url, data)
        self._log(name, rsp)
        return rsp

    @staticmethod
    def _log(name, rsp):
        logger.info('[{method}] {name} return {code} at {url}'.format(
            method=rsp.request.method, name=name, code=rsp.status_code, url=rsp.url
        ))

    @staticmethod
    def _get_random():
        return random() * 10 ** 8
