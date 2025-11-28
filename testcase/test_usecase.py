import pytest
import allure


from common.util.disassembly_requests_util import DisassemblyRequestUtil
from common.util.read_yaml_file_content import ReadYamlFileContent
from common.util.send_request import SendRequest

url = None
header = None
mothod = None
test_name = None
data = None

class TestUsercase():
   
    @allure.story("asd")
    def test_dsad(self):
        self.asdas()
    @allure.story("asdasdas")
    def asdas(self):
        return 1
    @pytest.mark.parametrize("date", ReadYamlFileContent().read_yaml_file_content_all())
    def test_data_driven(self,date):
        url, header, mothod, test_name, data = DisassemblyRequestUtil().disassembly_requests_util(date)
        self.user_case(url, header, mothod, test_name, data)



    @allure.feature("张三")
    @allure.story("lisi")
    @allure.title(url)
    @allure.testcase(url)
    @allure.description(test_name)
    def user_case(self,url, header, mothod, test_name, data):
        # SendRequest().url,SendRequest().header,SendRequest().mothod,SendRequest().test_name,SendRequest().data = res
        res1 = SendRequest().all_send_request(url, header, mothod, test_name, data)
        print(res1)
