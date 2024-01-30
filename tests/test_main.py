import pytest
from pages.home_page import MainPage


@pytest.mark.usefixtures('setup')
class TestMain:
    def test_main(self):
        home_page = MainPage(self.driver)
        home_page.get_signin_button().click()