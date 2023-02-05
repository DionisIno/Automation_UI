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

    class TestAlertsPage:

        def test_simple_alert(self, driver):
            simple_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            simple_alert.open()
            alert_text = simple_alert.simple_alert_button()
            assert alert_text == 'You clicked a button'

        def test_alert_after_five_second(self, driver):
            alert_after_five_second = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_after_five_second.open()
            alert_text = alert_after_five_second.alert_after_five_second()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_confirm_box(self, driver):
            comfirm_box_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            comfirm_box_alert.open()
            text_message = comfirm_box_alert.confirm_box()
            assert text_message == "You selected Cancel"

        def test_prompt_box(self, driver):
            prompt_box_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            prompt_box_alert.open()
            text_message, text = prompt_box_alert.prompt_box()
            assert text_message == f"You entered {text}"


    class TestFramePage:

        def test_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result1 = frame_page.check_frame('frame1')
            result2 = frame_page.check_frame('frame2')
            assert result1 == ['500px', '350px', 'This is a sample page'], "The frame does not exest"
            assert result2 == ['100px', '100px', 'This is a sample page'], "The frame does not exest"

    class TestNestedFrame:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            text_first_frame, text_second_frame = nested_frame_page.nested_frame_page()
            assert text_first_frame == "Parent frame", "The parent frame does not exist"
            assert text_second_frame == "Child Iframe", "The child frame does not exist"