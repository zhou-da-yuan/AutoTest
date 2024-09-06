import pytest

from common import env
from common.env import use
from common.login import Login


# 登录获取cookies
@pytest.fixture(scope="class", autouse=True)
def login_cookies():
    cookies = Login().get_cookie()
    return cookies


# 钩子函数，
def pytest_collection_modifyitems(items):
    for item in items:
        # 重新编码name和nodeid，以正确显示中文字符
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 自动获取更新environment.properties测试报告环境变量
env_data = env.read(use())


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    new_data = metadata
    new_data.update(env_data)
    """
       更新 environment.properties 文件，追加新的键值对，并保持原有键的顺序。

       :param file_path: environment.properties 文件的路径
       :param new_data: 包含新键值对的字典，可能包含嵌套字典
       """

    existing_lines = []
    try:
        with open('environment.properties', 'r') as file:
            for line in file:
                existing_lines.append(line.strip())
    except FileNotFoundError:
        print("The file does not exist. Creating a new one.")
        existing_lines = []

    # 从现有行中提取键值对，并存储到字典中
    existing_data = {}
    for line in existing_lines:
        if line:  # 确保行非空
            key, value = line.split('=', 1)  # 分割一次以确保值中也可以包含等号
            existing_data[key.strip()] = value.strip()

    # 检查新数据中是否存在不在原有文件中的键，并追加
    for key, value in new_data.items():
        if key not in existing_data:
            existing_lines.append(f'{key}={value}')

    # 将更新后的数据写回文件
    with open('environment.properties', 'w') as file:
        for line in existing_lines:
            file.write(f'{line}\n')
