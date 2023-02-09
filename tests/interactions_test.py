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

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            list_item = selectable_page.select_list_item()
            grid_item = selectable_page.select_grid_item()
            assert len(list_item) > 0
            assert len(grid_item) > 0

    class TestResizable:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            min_box, max_box = resizable_page.change_size_resaziable_box()
            min_page, max_page = resizable_page.change_size_resaziable()
            assert min_box != max_box
            assert min_page != max_page
