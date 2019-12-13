from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGO_PICT = (By.CSS_SELECTOR, ".card-block img[src='static/gh.jpg']")
    PAGE_HEADER = (By.CSS_SELECTOR, ".card-block strong h4.card-title")
    DESCRIPTION = (By.CSS_SELECTOR, ".card-block h5 small.text-muted")
    WS_MESSAGE = (By.CSS_SELECTOR, ".card-block #ws_msg")

class MainPageLocators():
    BUTTON_SHOW_ALL = (By.CSS_SELECTOR, "p a[href='/show_all'] button")
    SELECT_PAGINATE = (By.CSS_SELECTOR, "select#page_number")
    SELECT_PAGINATE_SET =(By.CSS_SELECTOR, "select#page_number option[value][select]")
    SELECT_PAGINATE_25 = (By.CSS_SELECTOR, "select#page_number option[value='25']")
    SELECT_PAGINATE_50 = (By.CSS_SELECTOR, "select#page_number option[value='50']")
    SELECT_PAGINATE_100 = (By.CSS_SELECTOR, "select#page_number option[value='100']")
    INPUT_SEARCH = (By.CSS_SELECTOR, "input#intitle")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn[type='Submit'][value='Search']")

class AnswerPageLocators():
    PAGE_NUMBER = (By.CSS_SELECTOR, ".card-block h5 strong") #:nth-child(2)
    BUTTON_HOME = (By.CSS_SELECTOR, "p a[href='/'] button")
    PAGE_RECORDS = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr")
    REC_IDS = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr td:nth-child(1)")
    REC_TOPICS = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr td:nth-child(2)")
    REC_AUTORS = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr td:nth-child(3)")
    REC_LINKS = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr td:nth-child(4)")
    REC_DATE_CREATE = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr td:nth-child(5)")
    REC_DATE_CHANGE = (By.CSS_SELECTOR, ".table.table-hover.table-striped tbody tr td:nth-child(6)")
    PAGES_NAVIGATION = (By.CSS_SELECTOR, ".for-group.row .btn.btn-info[name='page']")







class AllAnswersPageLocators():
    PAGE_HEADER = (By.CSS_SELECTOR, ".card-block strong h4.card-title")