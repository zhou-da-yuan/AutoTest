# 测试用例
import allure
import requests
import pytest
from requests import session

from common.case_yaml import yamlUtil
from common.env import read

# s = session()
# s.verify = False

base_url = read(181)['base_url']
user = read(181)['user']
password = read(181)['password']

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
    def test_search_user(self, s):
        response = s.request(
            'GET',
            url=base_url + '/console/consoleUser/list',
            params={
                "page": 1,
                "size": 20,
                "sortFiled": 'id',
                "sortOrder": 'asc'
            }
        )
        assert response.status_code == 200
        global id
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
