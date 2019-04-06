from abc import ABCMeta, abstractmethod
from functools import wraps
from random import random
from urllib import parse
from bs4 import BeautifulSoup

import requests

from utils.logger import get_logger

logger = get_logger()


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


def _take_qs(url):
    return parse.parse_qs(parse.urlsplit(url).query)


def _get_random():
    return random() * 10 ** 8


class JAccountLoginManager(metaclass=ABCMeta):
    def __init__(self, session=None):
        self.session = session or requests.Session()
        self.variables = self._fetch_variables()

    def new_session(self):
        self.session = requests.Session()
        self.variables = self._fetch_variables()

    @abstractmethod
    def get_login_url(self) -> str:
        pass

    @abstractmethod
    def check_login_result(self, rsp) -> 'error message':
        if 'jaccount.sjtu.edu.cn' in rsp.request.url:
            qs = _take_qs(rsp.request.url)
            err = qs.get('err', [''])[0]
            if err == '0':
                return '用户名或密码不正确'
            elif err == '1':
                return '验证码不正确'
            elif err == '2':
                return '服务器故障，请稍后再试'
            else:
                return '未知登录错误'
        return ''

    @with_max_retries(3)
    def get_captcha(self, nonce=None) -> ('content type', 'image blob'):
        captcha_url = 'https://jaccount.sjtu.edu.cn/jaccount/captcha?uuid={uuid}&t={t}'.format(
            uuid=self.variables['uuid'],
            t=nonce or _get_random()
        )
        rsp = self.session.get(captcha_url)
        return rsp.headers['Content-Type'], rsp.content

    @with_max_retries(3)
    def post_credentials(self, user, password, captcha) -> 'error message':
        action_url = 'https://jaccount.sjtu.edu.cn/jaccount/ulogin'
        payload = self.variables.copy()
        payload['user'] = user
        payload['pass'] = password
        payload['captcha'] = captcha
        rsp = self.session.post(action_url, payload)
        logger.info('login post return at: %s', rsp.request.url)
        return self.check_login_result(rsp)

    @with_max_retries(3)
    def _fetch_variables(self):
        rsp = self.session.get(self.get_login_url())
        logger.info('login page return at: %s', rsp.request.url)
        form = BeautifulSoup(rsp.text, 'html.parser').find(id='form-input')
        return {
            it.attrs['name']: it.attrs.get('value', '')
            for it in form.find_all('input', attrs={'name': True})
        }
