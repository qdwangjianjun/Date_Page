from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    data_path = "../data/MainPage.yaml"
    def gotoSelected(self):
        # #调用全局的driver对象使用webdriver api操纵app
        # #self.driver.find_element(By.xpath, "//*[@text='自选']")
        # zixuan="自选"
        # self.findByText(zixuan)
        # #self.driver.find_element_by_xpath("//*[@text='自选']")
        # self.findByText(zixuan).click()
        # return SelectedPage()
        self.load_yaml(MainPage.data_path, "gotoSelected")
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:
        # self.find(self._search_button).click()
        # return SearchPage()
        self.load_yaml(MainPage.data_path, "gotoSearch")
        return SearchPage()

    def gotoProfile(self):
        # self.find(MainPage._profile_button).click()
        # return ProfilePage()
        self.load_yaml(MainPage.data_path,"gotoProfile")
        return ProfilePage()