import pytest
from requests import session

from common.read_inter import inter


@pytest.fixture(scope='session', autouse=True)
def s():
    print('开始测试')
    s = session()
    s.verify = False
    yield s
    print('结束测试')
    s.close()


# @pytest.fixture(scope='function', autouse=True)
# def read_inter():
#     base_url = inter(181)['base_url']
#     user = inter(181)['user']
#     password = inter(181)['password']
#     yield

