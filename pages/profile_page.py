from base.selenium_base import SeleniumBase


class ProfilePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_order = '//button[contains(@data-bs-toggle, \'modal\')]'

    def get_order_button(self):
        return self.is_present('xpath', self.__xpath_order, 'Order button')