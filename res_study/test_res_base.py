import json
import os
import random
from functools import partial

import pytest
import requests
# @pytest.fixture()
# scope: "Union[_ScopeName, Callable[[str, Config], _ScopeName]]" = "function"         注释器作用域
# params: Optional[Iterable[object]] = None,                                           数据驱动
# autouse: bool = False,                                                                手动还是自动
# ids: Optional[                                                                        有数据驱动时更改别名
#     Union[Sequence[Optional[object]], Callable[[Any], Optional[object]]]
# ] = None,
# name: Optional[str] = None,                                                           别名
import yaml


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

    # @pytest.mark.parametrize("asd",[1,2,3,4,5,6,7])
    def test(self,x,y):
       return  x - y
    def test_asd(self):
        a = partial(self.test, 5)
        print(a(12))
    def test_dasd(self):

       res = random.choice([19520409998,19520409997])
       return res
    def test_yaml_dasdasd(self):
        print(yaml.safe_load(open('./test.yaml')))