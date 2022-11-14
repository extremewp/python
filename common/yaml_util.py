import os

# 读取yaml文件
import yaml


class YamlUtil:
    # 读取yaml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd() + 'extract.yaml') as f:
            return yaml.safe_load(stream=f, Loader=yaml.FullLoader)[key]

    # 写入yaml文件
    def writ_extract_yaml(self, date):
        with open(os.getcwd() + 'extract.yaml', 'wr') as f:
            yaml.safe_load(stream=f, data=date)

    # 清空yanl文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + 'extract.yaml', mode='r', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例
    def clear_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + '/testcase/' + yaml_name, mode='r', encoding='utf-8') as f:
          return yaml.safe_load(stream=f, Loader=yaml.FullLoader)