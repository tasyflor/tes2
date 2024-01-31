import pytest
from pages.home_page import MainPage
from pages.registration_page import RegistrationPage
from pages.profile_page import ProfilePage


@pytest.mark.usefixtures('setup')
class TestAuthorization:

    def test_authorization_faild(self):
        home_page = MainPage(self.driver)
        authorization_page = RegistrationPage(self.driver)

        name = 'Lorem Ipsum'
        password = 'passwordesssss'
        error_message = 'Input payload validation failed'

        home_page.get_signin_button().click()
        authorization_page.get_email_box().send_keys(name)
        authorization_page.get_password_box().send_keys(password)
        authorization_page.get_submit_button().click()
        error_text = authorization_page.get_error_message().text

        assert error_text == error_message

    def test_before_test_authorization(self):
        home_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)

        name = 'correct@email.ru'
        password = 'password'

        home_page.get_signup_button().click()
        registration_page.get_email_box().send_keys(name)
        registration_page.get_password_box().send_keys(password)
        registration_page.get_submit_button().click()
    def test_authorization(self):
        home_page = MainPage(self.driver)
        authorization_page = RegistrationPage(self.driver)
        profile_page = ProfilePage(self.driver)

        name = 'correct@email.ru'
        password = 'password'
        assert_text = "Заказать сервер"

        home_page.get_signin_button().click()
        authorization_page.get_email_box().send_keys(name)
        authorization_page.get_password_box().send_keys(password)
        authorization_page.get_submit_button().click()
        button = profile_page.get_order_button().text

        assert button == assert_text
