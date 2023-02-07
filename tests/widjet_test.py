import time
from pages.widjets_page import *

class TestWidjets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian(accordian_choice())
            assert title == "What is Lorem Ipsum?" or title == "Where does it come from?" or title == "Why do we use it?"
            assert len(content) > 0

    class TestAutoComplete:

        def test_multi_auto_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result

        def test_remove_auto_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            color_before, color_after = autocomplete_page.remove_value_multi()
            assert color_before != color_after

        def test_remove_all_colors(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = len(autocomplete_page.fill_input_multi())
            empty_input = autocomplete_page.remove_all_value()
            assert colors != 0
            assert empty_input is None

        def test_simple_color(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_single_auto_complete()
            check_color = autocomplete_page.check_single_color()
            assert color in check_color

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after


        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after