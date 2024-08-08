# 公共登录接口
import requests
from requests import session

from common import env
from common.env import read

import urllib3

from common.log import Log
from common.request import RunMethod

urllib3.disable_warnings()


class Login:

    def __init__(self):
        # 读取环境配置
        base = env.use()
        result = read(base)
        self.base_url = result['base_url']
        self.user = result['user']
        self.password = result['password']
        # 初始化接口请求
        self.ApiRun = RunMethod()

        self.log = Log()

    # 登录
    def login(self):
        try:
            response = self.ApiRun.api_run(
                'POST',
                url=self.base_url + '/console/doLogin',
                data={"user": self.user, "password": self.password}
            )
            self.log.info('登录成功-response = {}'.format(response.json()))
            return response
        except Exception as e:
            self.log.error('登录失败{}'.format(e))
            print(e)

    # 获取已登录的接口请求session
    def get_session(self):
        self.login()
        return self.ApiRun

    # 获取登录接口cookie
    def get_cookie(self):
        return Login.login(self).cookies

    # 关闭session
    def close_session(self):
        RunMethod().close_session()


if __name__ == '__main__':
    env.file = '../config/env.yaml'

    print(Login().get_session())
