from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")

class AlertsPageLocators:
    SIMPLE_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_BOX_ANSWER = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_BOX_ANSWER = (By.CSS_SELECTOR, "span[id='promptResult']")