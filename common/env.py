# 环境配置操作

import yaml

from common.log import Log

file = './config/env.yaml'
log = Log()


# 读取环境变量，返回字典
def read(env):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            log.info("读取env配置文件成功：{}".format(result[env]))
            return result[env]
    except Exception as e:
        log.warning("读取env配置文件出错{}".format(e))


# 增加环境变量，接收字典数据
def write(env, **kwargs):
    with open(file, 'r+', encoding='utf-8') as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
        s = result[env]
        for k, v in kwargs.items():
            s[k] = v
        with open(file, 'w', encoding='utf-8') as f:
            yaml.dump(result, f)


if __name__ == '__main__':
    file = '../config/env.yaml'
    print(read(119)['base_url'])
