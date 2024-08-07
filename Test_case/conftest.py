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