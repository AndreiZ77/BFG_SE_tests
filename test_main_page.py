# pytest -v --tb=line --language=en test_main_page.py
import pytest
import time
from .pages.main_page import MainPage
from .pages.answer_page import AnswerPage

link = "http://autotest-b8ns9mw7.bfg-soft.ru/" #BFG testing site


def test_guest_can_see_elements_of_main_page(browser):
    page = MainPage(browser, link, 3)
    page.open()
    page.should_be_header_elements()
    page.should_be_header_elements_with_main_page_values()
    page.should_be_interface_elements()

def test_guest_can_use_paginate_selector_of_main_page(browser):
    page = MainPage(browser, link, 3)
    page.open()
    page.set_paginate_value()

def test_guest_can_click_to_show_all(browser):
    page = MainPage(browser, link, 3)
    page.open()
    page.go_to_show_all()
    #time.sleep(3)

@pytest.mark.parametrize('page_limit', [25, 50, 100])
@pytest.mark.parametrize('search_text', ['python 3.8', 'c++', 'erunda', '14'])
def test_guest_can_search(browser, page_limit, search_text):
    page = MainPage(browser, link, 2)
    page.open()
    page.set_paginate_value(page_limit)
    page.input_search_and_click_submit(search_text)
    number_of_pages_to_test=3
    for i in range(number_of_pages_to_test):
        answer_page = AnswerPage(browser, browser.current_url, page_limit, search_text, i+1)
        answer_page.should_be_header_elements()
        answer_page.should_be_header_elements_with_answer_page_values()
        answer_page.number_records_equal_page_limit()
        answer_page.check_records_of_page()
        if answer_page.go_to_next_page() == False:
            break
