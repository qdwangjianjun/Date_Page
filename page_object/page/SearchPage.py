from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage

# By.CLASS_NAME
class SearchPage(BasePage):
    # _edit_locator=(By.CLASS_NAME, "android.widget.EditText")
    datafile="../data/SearchPage.yaml"
    def search(self, key):
        # self.find(self._edit_locator).send_keys(key)
        self.load_yaml(SearchPage.datafile,"search",var1 =key)
        return self

    def addToSelected(self, key):
        # follow_button = (By.XPATH,
        #                  "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
        #                  "//*[contains(@resource-id, 'follow_btn')]")
        #
        # self.find(follow_button).click()
        self.load_yaml(SearchPage.datafile,"addToSelected",var1 =key)

        return self


    def removeFromSelected(self, key):
        # followed_button = (By.XPATH,
        #                  "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
        #                  "//*[contains(@resource-id, 'followed_btn')]")
        #
        # self.find(followed_button).click()
        self.load_yaml(SearchPage.datafile,"removeFromSelected",var1 =key)
        return self

    def isInSelected(self, key):
        # follow_button=(By.XPATH,
        #                "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." %key +
        #                "//*[contains(@resource-id, 'follow')]")
        # id=self.find(follow_button).get_attribute("resourceId")
        # print(id)
        # return "followed_btn" in id
        self.load_yaml(SearchPage.datafile,"isInSelected",var1 =key)
        # print(BasePage.attribute_value.values())
        # print("followed_btn" in BasePage.attribute_value.values())
        # return "com.xueqiu.android:id/followed_btn" in BasePage.attribute_value.values()
        return "followed_btn" in BasePage.attribute_value

    def cancel(self):
        # self.findByText("取消").click()
        self.load_yaml(SearchPage.datafile,"cancel")

    def searchByUser(self, key):
        # todo: 作业2
        pass

    def isFollowed(self):
        # todo: 作业2
        pass