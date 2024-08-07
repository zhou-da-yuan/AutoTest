# 公共登录接口
from requests import session

from common import env
from common.env import read

import urllib3

urllib3.disable_warnings()


class Login:

    def __init__(self, env):
        self.env = env
        self.base_url = read(env)['base_url']
        self.user = read(env)['user']
        self.password = read(env)['password']
        s = session()
        s.verify = False
        self.s = s

    def login(self):
        response = self.s.request(
            'POST',
            url=self.base_url + '/console/doLogin',
            data={"user": self.user, "password": self.password}
        )

    # 获取登录接口cookie
    def get_cookie(self):
        Login.login(self)
        return self.s.cookies


if __name__ == '__main__':
    env.file = '../config/env.yaml'
    l = Login(119)
    for i in l.get_cookie():
        print(i)