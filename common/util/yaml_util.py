import importlib
import inspect
import os

import jinja2
# 读取yaml文件
import yaml
from yaml.constructor import ConstructorError
from yamlinclude import YamlIncludeConstructor


class YamlUtil:
    """
    用于yaml文件中调动方法
    渲染yaml文件
    """

    def render(self, yaml_rul_name, **kwargs):
        """渲染yml文件"""
        path, filename = os.path.split(yaml_rul_name)
        return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                                  ).get_template(filename).render(**kwargs)

    """
    用于yaml文件中调动方法
    加载方法文件
    """

    def all_functions(self, method_file_name):
        """加载debug.py模块"""
        debug_module = importlib.import_module(method_file_name)
        all_function = inspect.getmembers(debug_module, inspect.isfunction)
        print(dict(all_function))
        return dict(all_function)

    # 读取yaml文件
    def read_extract_yaml(self, resurl):

        with open(os.getcwd() + resurl) as f:
            return yaml.load(stream=f, Loader=yaml.FullLoader)

    # 写入yaml文件
    def writ_extract_yaml(self, date):
        with open(os.getcwd() + 'extract.yaml', 'wr') as f:
            yaml.safe_load(stream=f, data=date)

    # 清空yanl文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + 'extract.yaml', mode='r', encoding='utf-8') as f:
            f.truncate()

    """
    读yaml中测试用例
    若是yaml文件中没有调用python中方法则      method_file_name  可以不传
    若是yaml文件中有python中方法则 method_file_name 必传
    """
    def read_testcase_yaml(self, yaml_rul_name, method_file_name=None):
        YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
        if method_file_name == None:
            try:
                with open( yaml_rul_name, mode='r', encoding='utf-8') as f:
                    return yaml.load(stream=f, Loader=yaml.FullLoader)
            except ConstructorError :
                return "method_file_name必传为使用python文件名称"

        else:

            f = self.render(yaml_rul_name, **self.all_functions(method_file_name))
            return yaml.load(stream=f, Loader=yaml.FullLoader)
