import time

import pytest
from selenium.webdriver.common.by import By

from pages.header_section import design_nav_section


class TestDesignMenu:
    @pytest.fixture()
    def design(self, driver):
        return design_nav_section.DesignSection(driver)

    # Print all Design page titles and their links
    def test_design_nav_menu(self, design):
        design.navigate_to_kemet_page()
        time.sleep(2)
        design.accept_cookies()
        design.hover_over_design()
        time.sleep(2)

        number_of_design_sub_nav_items = design.get_design_items_count()
        print("\nDesign:")
        for i in range(1, number_of_design_sub_nav_items + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#subNav_3 > div.header__sub-nav-content > div > ul > li:nth-child(" + str(i) + ") > a"}
            design_nav_item_title = design.find_items(locator)
            print(design_nav_item_title.text)
            design_item_link = design_nav_item_title.get_attribute("href")
            design._visit2(design_item_link)
            assert design_item_link == design.get_current_url()
            design.navigate_to_kemet_page()
            design.hover_over_design()
