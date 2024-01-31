from base.selenium_base import SeleniumBase


class RegistrationPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_email = '//input[contains(@id, \'email\')]'
        self.__xpath_password = '//input[contains(@id, \'password\')]'
        self.__xpath_submit = '//button[contains(@type, \'submit\')]'
        self.__xpath_error = '//div[contains(@class, \'alert\')]/div'

    def get_email_box(self):
        return self.is_present('xpath', self.__xpath_email, 'Email box')

    def get_password_box(self):
        return self.is_present('xpath', self.__xpath_password, 'Password box')

    def get_submit_button(self):
        return self.is_present('xpath', self.__xpath_submit, 'Submit button')

    def get_error_message(self):
        return self.is_present('xpath', self.__xpath_error, 'Error message')

