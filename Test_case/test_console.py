import requests
import pytest
from requests import session
from com.read_con import read_json

base_data = read_json(r'..\config\config.json')
base_url = base_data['base_url']
user = base_data['user']
password = base_data['password']

s = session()
s.verify = False

class TestConsole:

    def test_login(self):
        response = s.request(
            'POST',
            url=base_url + '/console/doLogin',
            data={"user": user, "password": password}
        )
        assert response.status_code == 200
        print(response.cookies)
        print(response.text)

    def test_search_user(self):
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

    def test_user_detail(self):
        response = s.request(
            'GET',
            url=base_url + '/console/consoleUser/detail',
            params={
                "userId": id
            }
        )
        assert response.status_code == 200