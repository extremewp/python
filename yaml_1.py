# 基于类的解决方案，使用元类注册自定义构造函数。

import yaml

import os
import os.path

# 项目路径
project_path = os.path.split(os.path.realpath(__file__))[0].split('tools')[0]


class Loader(yaml.Loader):  # 继承
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include', Loader.include)


def get_yaml_data(fileDir):
    """
    读取 test.yaml 文件内容
    :param fileDir:
    :return:
    """
    # 1、在内存里加载这个文件
    # f = open(fileDir, 'r', encoding='utf-8')
    with open('./a.yaml', 'r') as f:
        data = yaml.load(f, yaml.Loader)
    print(data)

    # 2、调用yaml读取文件
    # Loader=yaml.FullLoader 更加安全
    res = yaml.load(f, Loader=yaml.FullLoader)
    return res


if __name__ == '__main__':
    info = get_yaml_data(project_path + r'\./a.yaml')
    print(info)

# 输出：
# {'a': 1,'b': [2, 3],'c': [10, [100,200, 300]]}
