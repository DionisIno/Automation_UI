from selenium.webdriver.common.by import By

class SortablePageLocators:
    LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class^='list-group-item']")
    GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "div[class='create-grid'] div[class^='list-group-item']")

class SelectablePageLocators:
    LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")
    GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")

class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[class='constraint-area'] span")
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] span")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")