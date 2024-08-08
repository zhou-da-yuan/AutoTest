# 测试用例
import pytest

from common import env
from common.case_yaml import yamlUtil

from common.env import read

from common.login import Login
from common.request import RunMethod


class TestConsole:
    s = RunMethod()
    base_url = read(env.use())['base_url']

    @pytest.mark.parametrize('params',
                             yamlUtil('./casedata/case.yaml').read_yaml()['search_user']['cases'])
    def test_search_user(self, login_cookies, params):
        response = self.s.api_run(
            'GET',
            url=self.base_url + '/console/consoleUser/list',
            params=params['case_params'],
            cookies=login_cookies
        )
        assert response.status_code == 200
        assert response.json()['success'] == True
        global id
        if not response.json()['success']:
            id = 0
        else:
            id = response.json()['users'][0]['id']

    def test_user_detail(self, login_cookies):
        response = self.s.api_run(
            'GET',
            url=self.base_url + '/console/consoleUser/detail',
            params={
                "userId": id
            },
            cookies=login_cookies
        )
        assert response.status_code == 200
