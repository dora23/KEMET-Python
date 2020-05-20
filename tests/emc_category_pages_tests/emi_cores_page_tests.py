import time

import pytest
from selenium.webdriver.common.by import By

from pages.emc_category_pages import emi_cores_page


class TestEmiCoresPage:
    @pytest.fixture()
    def emi_cores(self, driver):
        return emi_cores_page.EmiCoresPage(driver)

    def test_emi_cores_sub_categories(self, emi_cores):
        emi_cores.navigate_to_kemet_page()
        time.sleep(2)
        emi_cores.accept_cookies()
        emi_cores.hover_over_the_products_main_nav()
        emi_cores.hover_over_the_emc_sub_nav()
        emi_cores.click_on_emi_cores_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/emi-cores.html" == emi_cores.get_current_url()), \
            "This is not the EMI Cores page!"
        assert emi_cores.browse_tab_is_displayed()
        assert emi_cores.datasheets_tab_is_displayed()
        if emi_cores.emi_cores_category_slick_list_is_displayed:
            if emi_cores.all_emi_cores_displayed():
                time.sleep(2)
                emi_cores_slick_list_item_number = emi_cores.get_emi_cores_slick_list_items_count()
                print("\nEMI Cores Sub Categories:")
                for i in range(2, emi_cores_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = emi_cores.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
