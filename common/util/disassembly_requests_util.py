import requests

from common.util.yaml_util import YamlUtil


class DisassemblyRequestUtil:
    def __init__(self):
        self.session = requests.Session()
        self.yu = YamlUtil()
    def disassembly_requests_util(self, date):
        url = date["url"]
        data = date["date"]
        header = date["header"]
        mothod = date["method"]
        test_name = date["test_name"]
        self.yu.writ_extract_yaml(url="./common/date/usecase_name.yaml", date=test_name)
        return url, header, mothod, test_name, data