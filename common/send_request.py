import json
import time

import requests

from common.yaml_util import YamlUtil


class SendRequest:
    def __init__(self):
        self.session = requests.Session()
        self.yu = YamlUtil()
        self.time_date = str(round(time.time() * 1000))

    def all_send_request(self, url, data, header, mothod, **kwargs):

        mothod = str(mothod).lower()
        if mothod == 'get':
            res = self.session.request(url=url, params=data, headers=header, method=mothod, **kwargs)
        elif mothod == 'post':
            data = json.dumps(data)
            res = self.session.request(url=url, params=data, headers=header, method=mothod, **kwargs)

        return res.json()
