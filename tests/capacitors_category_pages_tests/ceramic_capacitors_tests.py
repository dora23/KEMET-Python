import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import ceramic_capacitor_page


class TestCeramicCapacitorPage:
    @pytest.fixture()
    def ceramic(self, driver):
        return ceramic_capacitor_page.CeramicCapacitorsPages(driver)

    # Test Ceramic Capacitor Slick Nav
    def test_ceramic_sub_categories(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/ceramic.html" == ceramic.get_current_url()), \
            "This is not the Ceramic Capacitor page!"
        if ceramic.ceramic_category_slick_list_is_displayed:
            if ceramic.all_ceramic_displayed():
                ceramic.click_on_slick_list_right_arrow()
                time.sleep(2)
                ceramic_slick_list_item_number = ceramic.get_ceramic_slick_list_items_count()
                print("\nCeramic Sub Categories:")
                for i in range(2, ceramic_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = ceramic.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
