import json

import requests


class TestResBase:
    def test_res(self):
        url = 'https://gatetest.googutwine.com/user/userLogin/getLoginGraphicVerificationCode'
        date = {"header": {"app_id": "10000001", "time_stamp": "1665730574364",
                           "transaction_type": "listUserEvaluationBill", "token": "7e17728f09d7a24a83960687a03c9f63",
                           "resources_id": "-999", "message_id": "1665730574364",
                           "imei": "671554c651cc966e7b9b12d693c2fb30", "terminal": "2", "version": "2.0.0"},
                "body": {"mobile": 17319420336}}
        header = {'Content-Type': 'application/json;charset=UTF-8'
                  }
        date = json.dumps(date)
        res = requests.session().request(method="post",url=url, data=date, headers=header)

