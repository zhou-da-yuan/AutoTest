import yaml

class yamlUtil():
    def __init__(self,yaml_file):

        '''
        通过init把文件传入到这个类
        :param yaml_file:
        '''
        self.yaml_file = yaml_file

    #读取ymal文件
    def read_yaml(self):
        '''
        读取yaml，将yaml反序列化，就是把我们yaml格式转换成dict格式
        :return:
        '''
        with open(self.yaml_file,encoding="utf-8") as f:
            value = yaml.load(f,Loader=yaml.FullLoader) #文件流，加载方式
            return value


if __name__ == '__main__':
    result = yamlUtil("../config/case.yaml").read_yaml()
    print(result)