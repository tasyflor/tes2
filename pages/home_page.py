from base.selenium_base import SeleniumBase


class MainPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_signin = '//a[contains(@href, \'/signin\')]'
        self.__xpath_signup = '//a[contains(@href, \'/signup\')]'
        self.__xpath_button = '//a[contains(@href, \'#\')]'
        self.__xpath_card = '//a[contains(@href, \'#\')]/../p'

    def get_signin_button(self):
        return self.is_present('xpath', self.__xpath_signin, 'Signin button')

    def get_signup_button(self):
        return self.is_present('xpath', self.__xpath_signup, 'Signup button')

    def get_server_card(self):
        return self.is_present('xpath', self.__xpath_card, 'Server card')

    def get_buy_button(self):
        return self.is_present('xpath', self.__xpath_button, 'Buy button')