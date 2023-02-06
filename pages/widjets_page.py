import base64
import os
import time
import random
import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
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

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators

    def fill_input_multi(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clicable(self.locators.MULTI_COLOR_NAMES)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_multi(self):
        count_value_before = len(self.elements_are_presents(self.locators.MULTI_COLOR_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_COLOR_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_presents(self.locators.MULTI_COLOR_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_presents((self.locators.MULTI_COLOR_VALUE))
        colors = []
        for i in color_list:
            colors.append(i.text)
        return colors

    def fill_single_auto_complete(self):
        color = random.sample(next(generator_color()).color_name, k=1)
        input_color = self.element_is_visible(self.locators.SINGLE_COLOR_INPUT)
        input_color.send_keys(color)
        input_color.send_keys(Keys.ENTER)
        return color[0]

    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_COLOR_NAME)
        return color.text

    def remove_all_value(self):
        empty_input = self.element_is_visible(self.locators.REMOVE_ALL_VALUE).click()
        return empty_input