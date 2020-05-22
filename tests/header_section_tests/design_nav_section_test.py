import time

import pytest
from selenium.webdriver.common.by import By

from pages.header_section import design_nav_section


class TestDesignMenu:
    @pytest.fixture()
    def design(self, driver):
        return design_nav_section.DesignSection(driver)

    # Print all Design page titles
    def test_products_nav_menu(self, design):
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
            product_nav_item_title = design.find_items(locator)
            print(product_nav_item_title.text)
