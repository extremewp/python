import os
import random

import jinja2
import yaml
import importlib
import inspect


def render(tpl_path, **kwargs):
    """渲染yml文件"""
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                              ).get_template(filename).render(**kwargs)


def all_functions():
    """加载debug.py模块"""
    debug_module = importlib.import_module("wahah1")
    all_function = inspect.getmembers(debug_module, inspect.isfunction)
    print(dict(all_function))
    return dict(all_function)


def rand_str():
    return str(random.randint(1000000, 2000000))


if __name__ == '__main__':
    r = render("a.yaml", **all_functions())
    print(r)
    print(yaml.safe_load(r))
