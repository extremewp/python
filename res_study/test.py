from functools import partial

import requests
import yaml


class Test:
    def test_asd(self):
        data = {
            "api": {
                "url": 'https://gatetest.googutwine.com/user/userLogin/getLoginGraphicVerificationCode',
                'mothod': 'post',
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           }
            },
            "case":
                [
                    [1, 3],
                    [2, 4],
                    [5, 6],
                ]
        }

        with open('test.yml', 'w') as f:
            yaml.safe_dump(data=data, stream=f)

    def test_pringt(self, x=1, y=2):
        return y

    def test_asdasd(self):
        api = partial(self.test_pringt, **yaml.safe_load(open("test.yml"))['api'])
        print(api)
        print(yaml.safe_load(open("test.yml"))['case'])
