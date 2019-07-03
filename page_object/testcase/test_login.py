from page_object.page.App import App
import pytest

class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage=App.main().gotoProfile()
    def setup_method(self):
        self.loginPage=self.profilePage.gotoLogin()

    @pytest.mark.parametrize("user, pw, msg", [
        ("156005347600", "111111", "手机号码填写错误"),
        ("15600534760", "111111", "用户名或密码错误")
    ])
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        # alert = self.loginPage.getErrorMsg().values()
        alert = self.loginPage.getErrorMsg()
        assert msg in alert

    def teardown_method(self):
        self.loginPage.back()