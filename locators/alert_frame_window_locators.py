from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")