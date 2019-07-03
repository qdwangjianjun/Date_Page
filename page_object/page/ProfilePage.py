from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    datapath="../data/ProfilePage.yaml"
    def gotoLogin(self):
        # self.findByText("点击登录").click()
        self.load_yaml(ProfilePage.datapath,"gotoLogin")
        return LoginPage()
