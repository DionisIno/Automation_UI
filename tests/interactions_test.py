import time
from pages.interactions_page import *


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before_list, after_list = sortable_page.change_list()
            before_grid, after_grid = sortable_page.change_grid()
            assert before_list != after_list
            assert before_grid != after_grid