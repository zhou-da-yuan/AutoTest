# 公共登录接口
from requests import session

from common import env
from common.env import read

import urllib3

from common.log import Log
from common.request import RunMethod

urllib3.disable_warnings()


class Login:

    def __init__(self, env):
        self.env = env
        result = read(env)
        self.base_url = result['base_url']
        self.user = result['user']
        self.password = result['password']
        self.log = Log()

    def login(self):
        try:
            response = RunMethod().api_run(
                'POST',
                url=self.base_url + '/console/doLogin',
                data={"user": self.user, "password": self.password}
            )
            self.log.info('登录成功response:{}'.format(response.json()))
            return response
        except Exception as e:
            self.log.error('登录失败{}'.format(e))
            print(e)

    # 获取登录接口cookie
    def get_cookie(self):
        return Login.login(self).cookies


if __name__ == '__main__':
    env.file = '../config/env.yaml'
    l = Login(119)

    print(l.get_cookie())