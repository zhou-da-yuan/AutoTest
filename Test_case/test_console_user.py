import allure
import pytest

from common import env
from common.case_yaml import yamlUtil
from common.env import read
from common.request import RunMethod


class TestUser:
    s = RunMethod()
    base_url = read(env.use())['base_url']

    @pytest.mark.parametrize('params',
                             yamlUtil('/casedata/case_console_user.yaml').read_yaml()['search_division']['cases'],
                             ids=[i['case_name'] for i in
                                  yamlUtil('/casedata/case_console_user.yaml').read_yaml()['search_division']['cases']]
                             )
    @allure.title("查询区域列表")
    def test_search_division(self, login_cookies, params):
        with allure.step('接口请求'):
            response = self.s.api_run(
                'GET',
                url=self.base_url + f'{yamlUtil('/casedata/case_console_user.yaml').read_yaml()["search_division"]["url"]}',
                params=params['case_params'],
                cookies=login_cookies
            )
            assert response.status_code == 200
            assert response.json()['success'] == True

        # 使用 allure 记录步骤
        with allure.step('查询默认区域是否存在'):
            allure.attach(f"Response status code: {response.status_code}","接口响应状态" )
            allure.attach(f"Response content: {response.text}", "接口响应内容")

            # 检查响应数据是否存在
            if response.json().get('data') is None:
                allure.attach("数据为空，断言失败")
                assert False, "响应中未找到数据"

            # 遍历数据，查找特定的 divisionCode
            found = False
            for region in response.json()['data']:
                if region.get('divisionCode') == '0000':
                    found = True
                    break

            if not found:
                allure.attach("未找到指定的 divisionCode: 0000","断言失败")
                assert False, "未找到指定的 divisionCode: 0000"

        # 如果执行到这里，则表示测试通过
        allure.attach("成功找到了指定的 divisionCode: 0000", "测试通过")

    @pytest.mark.parametrize('params',
                             yamlUtil('/casedata/case_console_user.yaml').read_yaml()['add_user']['cases'],
                             ids=[i['case_name'] for i in
                                  yamlUtil('/casedata/case_console_user.yaml').read_yaml()['add_user']['cases']]
                             )
    @allure.title("新增用户")
    def test_adduser(self, login_cookies, params):
        with allure.step('接口请求'):
            response = self.s.api_run(
                'POST',
                url=self.base_url + f'{yamlUtil('/casedata/case_console_user.yaml').read_yaml()["add_user"]["url"]}',
                data=params['case_params'],
                cookies=login_cookies
            )
            allure.attach(f"Response status code: {response.json()}","接口响应内容" )
            assert response.status_code == 200
            assert response.json()['success'] == True
