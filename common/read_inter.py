# 读取环境配置文件

import yaml

file = './config/config_inter.yaml'
def read_json():
    with open(file, 'r') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


def inter(inter):
    f = read_json()
    base_url = f[inter]['base_url']
    user = f[inter]['user']
    password = f[inter]['password']
    return {'base_url': base_url, 'user': user, 'password': password}


if __name__ == '__main__':
    file = '../config/config_inter.yaml'
    print(read_json())
    print(inter(181))
