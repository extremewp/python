import os

# 读取yaml文件
import yaml


def read_yaml():
    with open(os.getcwd()+'extract.yaml') as f:
        yaml.safe_load(f)

def writ_yaml(date):
    with open(os.getcwd()+'extract.yaml','wr') as f:
        yaml.safe_load(stream=f,data=date)