import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://localhost:4005'
service = [webdriver.Chrome(service=Service(ChromeDriverManager().install())),
           webdriver.Firefox(service=Service(GeckoDriverManager().install()))]


@pytest.mark.parametrize('browser_type', service)
class TestInfoBank:
    @classmethod
    def setup_class(cls):
        pass

    def test_test_test(self, browser_type):
        self.browser = browser_type
        self.wait = WebDriverWait(self.browser, 15)
        self.browser.get(URL)
        self.wait.until(EC.element_to_be_clickable(('id', 'card_bin'))).send_keys('533903')
        self.browser.find_element('id', 'get_info').click()
        self.browser.forward()
        bin_of_card = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(('xpath', "//table[@class='info_card']/tbody/tr/td")))
        assert bin_of_card.text == '533903', 'Fuck yourself!'
