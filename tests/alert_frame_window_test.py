import time

from pages.alert_frame_window_page import *



class TestAlertsFrameWindow:

    class TestBrowserWindow:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new tab is not find"


        def test_new_window(self, driver):
            new_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            text_result = new_window_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new window is not find"
