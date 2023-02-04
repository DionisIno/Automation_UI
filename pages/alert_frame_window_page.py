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

class AlertsPage(BasePage):
    locators = AlertsPageLocators

    def simple_alert_button(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def alert_after_five_second(self):
        self.element_is_visible(self.locators.ALERT_AFTER_FIVE_SECOND).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def confirm_box(self):
        self.element_is_visible(self.locators.CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
        text_message = self.element_is_present(self.locators.CONFIRM_BOX_ANSWER).text
        return text_message

    def prompt_box(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_message = self.element_is_present(self.locators.PROMPT_BOX_ANSWER).text
        return text_message, text
