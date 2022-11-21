import allure
import yaml


@allure.feature("用例我和你")
class TestStudentAllure:

    @allure.story("登录模块_成功")
    def test_asd(self):
        print('嗨嗨我登陆了-成功')

    @allure.story("登录模块_失败")
    def test_asd(self):
        print('嗨嗨我登陆了-失败')
    def test_yml(self):
        with open("../testcase/user.yaml") as f:
            print(yaml.safe_load(f))
