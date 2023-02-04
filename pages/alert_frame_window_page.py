import base64
import os
import time
import random
import requests
from selenium.webdriver.common.by import By
from generator.generator import *
from locators.alert_frame_window_locators import *
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_PAGE).text
        return text_title


    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_TAB_PAGE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_PAGE).text
        return text_title