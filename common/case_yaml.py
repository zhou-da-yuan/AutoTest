# 测试用例操作

import yaml

from common.log import Log


class yamlUtil():
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        self.log = Log()

    # 读取yaml文件
    def read_yaml(self):
        try:
            with open(self.yaml_file, encoding="utf-8") as f:
                value = yaml.load(f, Loader=yaml.FullLoader)
                self.log.info("读取yaml文件成功：{}".format(self.yaml_file))
                return value
        except Exception as e:
            self.log.error("读取yaml文件出错{}".format(e))
            print(e)


if __name__ == '__main__':
    result = yamlUtil("../casedata/case.yaml").read_yaml()
    print(result)
