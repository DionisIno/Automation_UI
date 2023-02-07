from selenium.webdriver.common.by import By

class AccordianPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, "div[id='section1Heading']")
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECOND_SECTION = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    THIRD_SECTION = (By.CSS_SELECTOR, "div[id='section3Heading']")
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section3Content'] p")

class AutoCompletePageLocators:
    MULTI_COLOR_NAMES = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_COLOR_VALUE = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value']")
    MULTI_COLOR_REMOVE = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value__remove']")
    REMOVE_ALL_VALUE = (By.CSS_SELECTOR, "div[class^='auto-complete__indicator'] svg")
    SINGLE_COLOR_NAME = (By.CSS_SELECTOR, "div[id='autoCompleteSingleContainer']")
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")

class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")