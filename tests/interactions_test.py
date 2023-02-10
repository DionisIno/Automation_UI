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

    class TestDroppable:

        def test_simple_droppable(self, driver):
            simple_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            simple_droppable_page.open()
            text = simple_droppable_page.drop_simple()
            assert text == "Dropped!"

        def test_accept_droppable(self, driver):
            accept_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            accept_droppable_page.open()
            accept, not_accept = accept_droppable_page.drop_accept()
            assert accept == "Dropped!"
            assert not_accept != "Dropped!"
        def test_prevent_droppable(self, driver):
            prevent_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            prevent_droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = prevent_droppable_page.drop_prevent()
            assert not_greedy == "Dropped!"
            assert not_greedy_inner == "Dropped!"
            assert greedy == "Outer droppable"
            assert greedy_inner == "Dropped!"

        def test_revert_droppable(self, driver):
            revert_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_will_revertable()
            assert before != after

        def test_not_revert_droppable(self, driver):
            revert_droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_not_revertable()
            assert before == after

