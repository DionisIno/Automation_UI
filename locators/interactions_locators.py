from selenium.webdriver.common.by import By

class SortablePageLocators:
    LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class^='list-group-item']")
    GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "div[class='create-grid'] div[class^='list-group-item']")