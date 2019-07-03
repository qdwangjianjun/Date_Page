from appium.webdriver.webdriver import WebDriver
from selenium import webdriver

class Test_XueQiu(object):
    driver:WebDriver
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path=r"E:\chromedriver\74.0.3729.6\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def setup_method(self):
        self.driver= Test_XueQiu.driver
        self.driver.get("https://xueqiu.com/")

    def test_Search(self):
        self.driver.find_element_by_css_selector('input[placeholder=搜索]').clear()
        self.driver.find_element_by_css_selector('input[placeholder=搜索]').send_keys("阿里巴巴")
        self.driver.find_element_by_css_selector('.icon.iconfont').click()
        self.driver.find_element_by_xpath('//*[text() = "01688"]/../../../..//*[@class="follow__control"]').click()
        self.driver.find_element_by_name("username").send_keys("tudou")
        self.driver.find_element_by_name("password").send_keys("tudou")
        self.driver.find_element_by_xpath('//*[@class="modal__login__btn" and contains(text(),"登") and contains(text(),"录")]').click()


