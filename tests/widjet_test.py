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