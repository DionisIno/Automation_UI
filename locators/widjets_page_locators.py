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