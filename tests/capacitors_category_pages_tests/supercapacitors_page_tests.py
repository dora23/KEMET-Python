import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import supercapacitors_page


class TestSupercapacitorsPage:
    @pytest.fixture()
    def super(self, driver):
        return supercapacitors_page.SuperCapacitorsPage(driver)

    # Test Supercapacitors Slick Nav
    def test_supercapacitors_sub_categories(self, super):
        super.navigate_to_kemet_page()
        time.sleep(2)
        super.accept_cookies()
        super.hover_over_the_products_main_nav()
        super.hover_over_the_capacitors_sub_nav()
        super.click_on_supercapacitors_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/supercapacitors.html" == super.get_current_url()), \
            "This is not the Supercapacitor page!"
        if super.supercapacitors_category_slick_list_is_displayed:
            if super.all_supercapacitors_displayed():
                supercapacitors_slick_list_item_number = super.get_supercapacitors_slick_list_items_count()
                print("\nFilm Capacitors Sub Categories:")
                for i in range(2, supercapacitors_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = super.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Supercapacitors tab is not displayed")
        else:
            print("The Slick list is not displayed")
