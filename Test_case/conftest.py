import pytest
from common import env
from common.case_yaml import yamlUtil
from common.login import Login


# 登录获取cookies
@pytest.fixture(scope="class", autouse=True)
def login_cookies():
    cookies = Login().get_cookie()
    return cookies


def pytest_html_report_title(report):
    report.title = "My very own title!"


# 钩子函数，
def pytest_collection_modifyitems(items):
    for item in items:
        # 重新编码name和nodeid，以正确显示中文字符
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
