import time

import pytest
from selenium.webdriver.common.by import By

from pages.emc_category_pages import dc_chokes_page


class TestDcChokesPage:
    @pytest.fixture()
    def dc_chokes(self, driver):
        return dc_chokes_page.DcChokesPage(driver)

    def test_dc_chokes_sub_categories(self, dc_chokes):
        dc_chokes.navigate_to_kemet_page()
        time.sleep(2)
        dc_chokes.accept_cookies()
        dc_chokes.hover_over_the_products_main_nav()
        dc_chokes.hover_over_the_emc_sub_nav()
        dc_chokes.click_on_dc_chokes_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/dc-chokes.html" == dc_chokes.get_current_url()), \
            "This is not the DC Chokes page!"
        assert dc_chokes.browse_tab_is_displayed()
        assert dc_chokes.datasheets_tab_is_displayed()
        if dc_chokes.dc_chokes_category_slick_list_is_displayed:
            if dc_chokes.all_dc_chokes_displayed():
                time.sleep(2)
                dc_chokes_slick_list_item_number = dc_chokes.get_dc_chokes_slick_list_items_count()
                print("\nDC Chokes Sub Categories:")
                for i in range(2, dc_chokes_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = dc_chokes.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
