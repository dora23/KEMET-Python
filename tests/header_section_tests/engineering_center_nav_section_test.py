import time

import pytest
from selenium.webdriver.common.by import By

from pages.header_section import engineering_center_nav_section


class TestEngineeringCenterMenu:
    @pytest.fixture()
    def engineering(self, driver):
        return engineering_center_nav_section.EngineeringCenterSection(driver)

    # Print all Engineering Center page titles and verify their link
    def test_engineering_center_nav_menu(self, engineering):
        engineering.navigate_to_kemet_page()
        time.sleep(2)
        engineering.accept_cookies()
        engineering.hover_over_engineering_center()
        time.sleep(2)

        number_of_eng_center_sub_nav_items = engineering.get_engineering_center_items_count()
        print("\nEngineering Center:")
        for i in range(1, number_of_eng_center_sub_nav_items + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#subNav_4 > div.header__sub-nav-content > div > ul > li:nth-child(" + str(i) + ") > a"}
            engineering_nav_item_title = engineering.find_items(locator)
            print(engineering_nav_item_title.text)
            engineering_item_link = engineering_nav_item_title.get_attribute("href")
            engineering._visit2(engineering_item_link)
            if engineering_item_link.endswith('/'):
                assert engineering_item_link == engineering.get_current_url()
            else:
                item_url = (engineering_item_link + '/')
                assert item_url == engineering.get_current_url()
            engineering.navigate_to_kemet_page()
            engineering.hover_over_engineering_center()
