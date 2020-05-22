import time

import pytest
from selenium.webdriver.common.by import By

from pages.header_section import engineering_center_nav_section


class TestEngineeringCenterMenu:
    @pytest.fixture()
    def engineering(self, driver):
        return engineering_center_nav_section.EngineeringCenterSection(driver)

    # Print all Engineering Center page titles
    def test_products_nav_menu(self, engineering):
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
