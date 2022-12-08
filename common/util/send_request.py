import json
import time

import allure
import requests

from common.util.yaml_util import YamlUtil


class SendRequest:

    def __init__(self):
        self.session = requests.Session()
        self.yu = YamlUtil()




    def all_send_request(self, url, header, mothod, test_name, data):
        self.time_date = str(round(time.time() * 1000))
        test_name = test_name
        mothod = str(mothod).lower()
        if mothod == 'get':
            res = self.session.request(url=url, params=data, headers=header, method=mothod)
        elif mothod == 'post':
            data = json.dumps(data)
            res = self.session.request(url=url, data=data, headers=header, method=mothod)
        if "file" in data:
            res = self.session.request(url=url, files=data, headers=header, method=mothod)
        return res
