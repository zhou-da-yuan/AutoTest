# 测试用例

from common import env

from common.env import read

from common.login import Login


class TestConsole:

    def setup_class(self):
        # 初始化登录，获取session
        base = env.use()
        self.base_url = read(base)['base_url']
        self.s = Login().get_session()

    def teardown_class(self):
        self.s.close_session()

    def test_search_user(self):
        response = self.s.api_run(
            'GET',
            url=self.base_url + '/console/consoleUser/list',
            params={
                "page": 1,
                "size": 10,
                "sortFiled": 'id',
                "sortOrder": 'asc'
            }
        )
        assert response.status_code == 200
        global id
        if not response.json()['success']:
            id = 0
        else:
            id = response.json()['users'][0]['id']

    def test_user_detail(self):
        response = self.s.api_run(
            'GET',
            url=self.base_url + '/console/consoleUser/detail',
            params={
                "userId": id
            }
        )
        assert response.status_code == 200
