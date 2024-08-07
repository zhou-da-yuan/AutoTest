import pytest
from requests import session



@pytest.fixture(scope='session', autouse=True)
def s():
    print('开始测试')
    s = session()
    s.verify = False
    yield s
    print('结束测试')
    s.close()



def pytest_html_report_title(report):
    report.title = "My very own title!"


# 钩子函数，
def pytest_collection_modifyitems(items):
    for item in items:
        # 重新编码name和nodeid，以正确显示中文字符
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")