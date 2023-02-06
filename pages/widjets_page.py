import base64
import os
import time
import random
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from generator.generator import *
from locators.widjets_page_locators import *
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    def check_accordian(self, accordian_number):
        accordian = {'first':
                         {'title': self.locators.FIRST_SECTION,
                          'content': self.locators.FIRST_SECTION_TEXT},
                     'second':
                         {'title': self.locators.SECOND_SECTION,
                          'content': self.locators.SECOND_SECTION_TEXT},
                     'third':
                         {'title': self.locators.THIRD_SECTION,
                          'content': self.locators.THIRD_SECTION_TEXT}
                     }
        section_title = self.element_is_visible(accordian[accordian_number]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
        return [section_title.text, section_content]