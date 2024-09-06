# 测试用例操作
import os
import re

import faker
import yaml

from common.log import Log
from common.faker_data import *

faker = faker.Faker('zh_CN')


class yamlUtil():

    def __init__(self, yaml_file):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.yaml_file = self.BASE_PATH + yaml_file
        self.log = Log()

    # 读取yaml文件
    def read_yaml(self):
        try:
            with open(self.yaml_file, encoding="utf-8") as f:
                value = yaml.load(f, Loader=yaml.FullLoader)
                self.log.info("读取yaml文件成功：{}".format(self.yaml_file))
                value = self.replace_placeholders(value)
                return value
        except Exception as e:
            self.log.error("读取yaml文件出错{}".format(e))
            print(e)

    # 替换占位符
    def replace_placeholders(self,data):
        """
        递归遍历数据结构，查找并替换字符串中的占位符。
        占位符格式为 ${method_call}，其中 method_call 是 Faker 对象的方法调用。
        """
        try:
            # 遍历数据结构中的键值对
            for key, value in data.items():
                # 如果值是一个字典，继续处理
                if isinstance(value, dict):
                    self.replace_placeholders(value)

                # 如果值是一个列表，递归处理
                elif isinstance(value, list):
                    for item in value:
                        self.replace_placeholders(item)

                # 如果值是一个字符串，提取并替换占位符
                elif isinstance(value, str):
                    placeholders = re.findall(r'\$\{.*?\}', value)
                    for placeholder in placeholders:
                        # 移除 ${ 和 } 并执行方法
                        method_call = placeholder[2:-1]
                        try:
                            # 执行方法调用，并获取结果
                            result = eval(method_call)
                            # 替换占位符
                            value = value.replace(placeholder, str(result))
                            # 将替换后的值保存到原始数据中
                            data[key] = value

                        except Exception as e:
                            print(f"Error executing {method_call}: {e}")
            return data
        except Exception as e:
            print('替换占位符发生错误：' + str(e))


if __name__ == '__main__':
    result = yamlUtil("/casedata/case_console_user.yaml").read_yaml()
    print(result)
    print(RandomDataGenerator().numerify())
