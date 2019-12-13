from .base_page import BasePage
from .locators import BasePageLocators, AnswerPageLocators

class AnswerPage(BasePage):
    def __init__(self, browser, link, page_limit, search_text, page_number):
        self.browser = browser
        self.link = link
        self.page_limit = page_limit
        self.page_number = page_number
        self.search_text = search_text

    def should_be_header_elements_with_answer_page_values(self):
        assert self.browser.find_element(*BasePageLocators.PAGE_HEADER).text == 'Результаты запроса:', \
            "Page header value is not correct"
        assert self.browser.find_element(*BasePageLocators.DESCRIPTION).text == 'Ну что же, приступим.', \
            "Page description value is not correct"
        page_number_value = self.browser.find_element(*AnswerPageLocators.PAGE_NUMBER).text.split(' ')[1]
        assert int(page_number_value) == self.page_number, \
            f"Page number value {page_number_value} is not equal {self.page_number}"

    def number_records_equal_page_limit(self):
        number_of_records = len(self.browser.find_elements(*AnswerPageLocators.PAGE_RECORDS))
        if number_of_records > 0:
            if len(self.browser.find_elements(*AnswerPageLocators.PAGES_NAVIGATION)) == 1:
                assert number_of_records <= self.page_limit, \
                    f"Number of records per page {number_of_records} is higher than the page limit:{self.page_limit}"
            elif len(self.browser.find_elements(*AnswerPageLocators.PAGES_NAVIGATION)) == 2:
                assert number_of_records == self.page_limit, \
                    f"Number of records per page {number_of_records} is not equal the page limit:{self.page_limit}"

    def check_records_of_page(self):
        rec_ids = self.browser.find_elements(*AnswerPageLocators.REC_IDS)
        true_id = (self.page_number - 1) * self.page_limit
        rec_topics = self.browser.find_elements(*AnswerPageLocators.REC_TOPICS)
        for i in range(len(rec_ids)):
            true_id += 1
            assert int(rec_ids[i].text) == true_id, f"id of records {rec_ids[i].text} is not equal {true_id}"
            topic_text = rec_topics[i].text.lower()
            search_text_parts =self.search_text.lower().split(' ')
            contain = False
            for i in range(len(search_text_parts)):
                if search_text_parts[i] in topic_text:
                    contain = True
            assert contain, f"topic:'{topic_text}' does not contain the parts of search text:'{self.search_text}'"

    def go_to_next_page(self):
        if len(self.browser.find_elements(*AnswerPageLocators.REC_IDS)) == 0:
            return False
        nav_buttons = self.browser.find_elements(*AnswerPageLocators.PAGES_NAVIGATION)
        if len(nav_buttons) == 2:
            next_button = nav_buttons[1]
        elif len(nav_buttons) == 1:
            next_button = nav_buttons[0]
        elif len(nav_buttons) == 0:
            raise AssertionError("Buttons 'previous' and 'next' is not presented")
            return False

        if int(next_button.get_attribute("value")) > self.page_number:
            next_button.click()
            return True







