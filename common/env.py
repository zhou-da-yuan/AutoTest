# 环境配置操作

import yaml

file = './config/env.yaml'


# 读取环境变量，返回字典
def read(env):
    with open(file, 'r', encoding='utf-8') as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
        return result[env]


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
