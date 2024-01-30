import pytest
import faker
from pages.home_page import MainPage
from pages.registration_page import RegistrationPage
from pages.profile_page import ProfilePage


@pytest.mark.usefixtures('setup')
class TestRegistration:
    def test_registration_name_password(self):
        home_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)

        name = 'Lorem Ipsum'
        password = 'password'
        error_message = 'Input payload validation failed'

        home_page.get_signup_button().click()
        registration_page.get_email_box().send_keys(name)
        registration_page.get_password_box().send_keys(password)
        registration_page.get_submit_button().click()
        error_text = registration_page.get_error_message().text

        assert error_text == error_message

    def test_registration_wrong_email_password(self):
        home_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)

        email = 'test@'
        password = 'password'
        error_message = 'Input payload validation failed'

        home_page.get_signup_button().click()
        registration_page.get_email_box().send_keys(email)
        registration_page.get_password_box().send_keys(password)
        registration_page.get_submit_button().click()
        error_text = registration_page.get_error_message().text

        assert error_text == error_message

    def test_registration_empty_password(self):
        home_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)

        name = 'Lorem Ipsum'
        password = ''

        home_page.get_signup_button().click()
        registration_page.get_email_box().send_keys(name)
        registration_page.get_password_box().send_keys(password)
        registration_page.get_submit_button().click()
        button_visible = registration_page.get_submit_button().is_displayed()

        # If submit button presented, test passed, cause we still placed at registration page
        assert button_visible == True

    def test_successful_registration(self):
        home_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)
        profile_page = ProfilePage(self.driver)

        f = faker.Faker()
        fake_mail = f.email()
        password = 'qweasdzxc'
        assert_text = "Заказать сервер"

        home_page.get_signup_button().click()
        registration_page.get_email_box().send_keys(fake_mail)
        registration_page.get_password_box().send_keys(password)
        registration_page.get_submit_button().click()

        button = profile_page.get_order_button().text

        assert button == assert_text

    def test_unsuccessful_registration(self):
        home_page = MainPage(self.driver)
        registration_page = RegistrationPage(self.driver)
        profile_page = ProfilePage(self.driver)

        email = 'test@test.uz'
        password = 'zxcvbn'
        assert_text = 'test@test.uz is already registered'
        home_page.get_signup_button().click()
        registration_page.get_email_box().send_keys(email)
        registration_page.get_password_box().send_keys(password)
        registration_page.get_submit_button().click()

        error_text = registration_page.get_error_message().text

        assert error_text == assert_text