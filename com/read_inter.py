import yaml


def read_json():
    with open('D:/Pycharm/Spytest/config/config_inter.yaml', 'r') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


def inter(inter):
    f = read_json()
    base_url = f[inter]['base_url']
    user = f[inter]['user']
    password = f[inter]['password']
    return {'base_url': base_url, 'user': user, 'password': password}


if __name__ == '__main__':
    print(read_json())
    print(inter(181))
