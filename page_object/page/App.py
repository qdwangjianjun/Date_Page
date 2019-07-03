from page_object.driver.Client import Client
from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().install_app()
        return MainPage()