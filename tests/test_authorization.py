import pytest
from pages.home_page import MainPage
from pages.registration_page import RegistrationPage


@pytest.mark.usefixtures('setup')
class TestAuthorization:
    def test_authorization(self):
        home_page = MainPage(self.driver)
        home_page.get_signup_button().click()
