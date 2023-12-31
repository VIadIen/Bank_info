import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://localhost:4000'
service = [webdriver.Chrome(service=Service(ChromeDriverManager().install())),
           webdriver.Firefox(service=Service(GeckoDriverManager().install()))]


@pytest.mark.parametrize('browser_type', service)
class TestInfoBank:
    def test_end_2_end(self, browser_type):
        self.browser = browser_type
        self.wait = WebDriverWait(self.browser, 15)
        self.browser.get(URL)
        self.wait.until(EC.element_to_be_clickable(('id', 'card_bin'))).send_keys('533903')
        self.browser.find_element('id', 'get_info').click()
        bin_of_card = self.wait.until(
            EC.text_to_be_present_in_element(('xpath', "//table[@class='info_card']/tbody/tr/td"), '533903'))
        assert bin_of_card, 'Incorrect answer!'

    def test_pass_field(self, browser_type):
        self.browser = browser_type
        self.wait = WebDriverWait(self.browser, 15)
        self.browser.get(URL)
        self.browser.find_element('id', 'get_info').click()
        status = self.wait.until(
            EC.visibility_of_element_located(("tag name", "h1"))).text  # fixed ERROR
        self.browser.quit()
        assert status == '404 Not Found', 'Incorrect answer!'
