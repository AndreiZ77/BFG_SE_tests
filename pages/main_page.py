from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .locators import BasePageLocators, MainPageLocators

class MainPage(BasePage):
    def should_be_header_elements_with_main_page_values(self):
        assert self.browser.find_element(*BasePageLocators.PAGE_HEADER).text == 'StackOverSearch', \
            "Page header value is not correct"
        assert self.browser.find_element(*BasePageLocators.DESCRIPTION).text == 'Быстрый поиск по StackExchange API', \
            "Page description value is not correct"


    def should_be_interface_elements(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_SHOW_ALL), "'Show all' button is not presented"
        assert self.is_element_present(*MainPageLocators.SELECT_PAGINATE), "Paginate selector is not presented"
        assert self.is_element_present(*MainPageLocators.SELECT_PAGINATE_25), "Paginate selector value=25 is not presented"
        assert self.is_element_present(*MainPageLocators.SELECT_PAGINATE_50), "Paginate selector value=50 is not presented"
        assert self.is_element_present(*MainPageLocators.SELECT_PAGINATE_100), "Paginate selector value=100 is not presented"
        assert self.is_element_present(*MainPageLocators.INPUT_SEARCH), "Search line is not presented"
        assert self.is_element_present(*MainPageLocators.BUTTON_SUBMIT), "Search submit button is not presented"

    def set_paginate_value(self, page_limit=25):
        select = Select(self.browser.find_element(*MainPageLocators.SELECT_PAGINATE))
        select.select_by_value(str(page_limit))

        #mySelect = Select(driver.find_element_by_id("mySelectID"))
        # option = mySelect.first_selected_option
        # print option.text  #prints "Option"
        #mySelect = Select(driver.find_element_by_id("mySelectID"))
        #print [o.text for o in mySelect.options] #Prints "Option", followed by "Not Option"

    def go_to_show_all(self):
        self.browser.find_element(*MainPageLocators.BUTTON_SHOW_ALL).click()

    def input_search_and_click_submit(self, search_text=''):
        self.browser.find_element(*MainPageLocators.INPUT_SEARCH).send_keys(search_text)
        self.browser.find_element(*MainPageLocators.BUTTON_SUBMIT).click()



