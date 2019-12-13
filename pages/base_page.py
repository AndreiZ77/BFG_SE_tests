from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from urllib.parse import urlparse





class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4): # элемент не появится на странице, плюсом к проверке на наличие
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4): # проверить, что какой-то элемент исчезает
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def get_url_parts(self):
        #ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html' ,params='', query='', fragment='')
        url_parts = urlparse(self.url)
        return url_parts

    def alert_get(self):
        alert = self.browser.switch_to.alert
        # x = alert.text.split(" ")[2]
        # answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def should_be_header_elements(self):
        assert self.is_element_present(*BasePageLocators.LOGO_PICT), "LOGO is not presented"
        assert self.is_element_present(*BasePageLocators.PAGE_HEADER), "Page header is not presented"
        assert self.is_element_present(*BasePageLocators.DESCRIPTION), "Page description is not presented"
        assert self.is_element_present(*BasePageLocators.WS_MESSAGE), "WS-message string is not presented"



