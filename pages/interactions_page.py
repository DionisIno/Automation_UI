import base64
import os
import time
import random
import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import *
from locators.interactions_locators import *
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators

    def get_sortable_items(self, elem):
        item_list = self.elements_are_visible(elem)
        return [item.text for item in item_list]

    def change_list(self):
        self.element_is_visible(self.locators.LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=3)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid(self):
        self.element_is_visible(self.locators.GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=3)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after

class SelectablePage(BasePage):
    locators = SelectablePageLocators

    def click_selected_item(self, elem):
        item_list = self.elements_are_visible(elem)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.LIST).click()
        self.click_selected_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID).click()
        self.click_selected_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text

class ResizablePage(BasePage):
    locators = ResizablePageLocators

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_and_min_size(self, elem):
        size = self.element_is_present(elem)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resaziable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -200)
        min_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resaziable(self):
        qw = self.element_is_present(self.locators.RESIZABLE_HANDLE)
        self.go_to_element(qw)
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 500), random.randint(1, 500))
        max_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-500, -1), random.randint(-500, -1))
        min_size = self.get_px_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE))
        return max_size, min_size
