from selenium.webdriver.common.by import By



class TextBoxPageLocators:

    #form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id = 'userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id = 'userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id ='submit']")

    #created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:

    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")

class WebTablePageLocators:
    #add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_REG = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_REG = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_REG = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_REG = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_REG = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_REG = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON =  (By.CSS_SELECTOR, "button[id='submit']")

    #table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"