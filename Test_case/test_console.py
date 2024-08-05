# 测试用例


import requests
import pytest
from requests import session
from common.read_inter import inter

# s = session()
# s.verify = False

base_url = inter(181)['base_url']
user = inter(181)['user']
password = inter(181)['password']


class TestConsole:
    def test_login(self, s):
        response = s.request(
            'POST',
            url=base_url + '/console/doLogin',
            data={"user": user, "password": password}
        )
        assert response.status_code == 200
        assert response.json()['success'] == True

    def test_search_user(self, s):
        response = s.request(
            'GET',
            url=base_url + '/console/consoleUser/list',
            params={
                "page": 1,
                "size": 50,
                "sortFiled": "id",
                "sortOrder": "asc"
            }
        )
        assert response.status_code == 200
        global id
        id = response.json()['users'][0]['id']

    def test_user_detail(self, s):
        response = s.request(
            'GET',
            url=base_url + '/console/consoleUser/detail',
            params={
                "userId": id
            }
        )
        assert response.status_code == 200
