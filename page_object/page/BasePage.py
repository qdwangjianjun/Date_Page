import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.Client import Client


class BasePage(object):
    # attribute_value={}
    attribute_value:str
    backslist =[("xpath","//*[@text='下次再说']")]
    def __init__(self):
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=Client.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return Client

    def find(self, by,locator) -> WebElement:
        #todo: 处理各类弹框
        for i in  range(3):
            try:
                element=self.driver.find_element(by,locator)
                return element
            except:
                for e in BasePage.backslist:
                    elements = self.driver.find_elements(*e)
                    if len(elements) > 0:
                        elements[0].click()
    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))


    def load_yaml(self,filepath,funckey,**kwargs):
        with open(filepath,mode="r",encoding="utf-8") as f:
            data = yaml.load(f)
        data_func = data[funckey]
        for step in data_func:
            if "element" in step.keys():
                platfrom_element = data["platfrom_elements"][step["element"]][Client.platform]
                locator = platfrom_element["locator"]
                for k,v in kwargs.items():
                    locator = str(locator.replace("$%s"%k,v))
                by = platfrom_element["by"]
            else:
                locator =str(step["locator"])
                for k,v in kwargs.items():
                    locator = locator.replace("$%s"%k,v)
                    print(locator)
                by = step["by"]
            element:WebElement = self.find(by,locator)
            action = str(step["action"]).lower()
            if "click" in action:
                element.click()
            elif "sendkeys" in action:
                text = str(step["text"])
                for k,v in kwargs.items():
                    text = text.replace("$%s"%k,v)
                element.send_keys(text)
            elif "get_attribute" in action:
                attribute = str(step["attribute"])
                # for k,v in kwargs.items():
                #     attribute = attribute.replace("$%s"%k,v)
                # BasePage.attribute_value[locator] = element.get_attribute(attribute)
                BasePage.attribute_value= element.get_attribute(attribute)




