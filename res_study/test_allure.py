import allure


@allure.feature('123')
class TestAllure:

    @allure.story("登录成功")
    def test_asd(self):
        print('登录成功')

    @allure.story("登录失败")
    def test_asc(self):
        print('登录失败')
