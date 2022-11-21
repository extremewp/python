import hashlib
import json
import time


class SignUtil:
    def sign_api(self, date, date_time):

        key = "fe6bd6d1"
        datas = (key + date + date_time)
        m = hashlib.md5()
        m.update(datas.encode("utf8"))
        sign = m.hexdigest()
        return sign
