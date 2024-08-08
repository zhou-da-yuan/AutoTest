# 测试用例
import allure
import requests
import pytest
from requests import session

from common.case_yaml import yamlUtil
from common.env import read

# s = session()
# s.verify = False

env = read(119)

base_url = env['base_url']
user = env['user']
password = env['password']

@allure.title('运营端')
class TestConsole:
    @allure.step('登录')
    def test_login(self, s):
        response = s.request(
            'POST',
            url=base_url + '/console/doLogin',
            data={"user": user, "password": password}
        )
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.step('搜索用户')
    @pytest.mark.parametrize('case',
                             yamlUtil('./casedata/case.yaml').read_yaml()['search_user']['cases'],
                             ids=[i['case_name'] for i in yamlUtil('./casedata/case.yaml').read_yaml()['search_user']['cases']],
                             )
    def test_search_user(self, s, case):
        response = s.request(
            'GET',
            url=base_url + '/console/consoleUser/list',
            params={
                "page": case['case_params']['page'],
                "size": case['case_params']['size'],
                "sortFiled": case['case_params']['sortFiled'],
                "sortOrder": case['case_params']['sortOrder']
            }
        )
        assert response.status_code == 200
        global id
        if response.json()['success'] == False:
            id = 0
        else:
            id = response.json()['users'][0]['id']

    @allure.step('用户详情')
    def test_user_detail(self, s):
        response = s.request(
            'GET',
            url=base_url + '/console/consoleUser/detail',
            params={
                "userId": id
            }
        )
        assert response.status_code == 200
