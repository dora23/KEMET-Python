import time

import pytest
from selenium.webdriver.common.by import By

from pages.emc_category_pages import emi_rfi_filters_page


class TestEmiRfiFiltersPage:
    @pytest.fixture()
    def emi_rfi_filters(self, driver):
        return emi_rfi_filters_page.EmiRfiFiltersPage(driver)

    def test_emi_rfi_filters_sub_categories(self, emi_rfi_filters):
        emi_rfi_filters.navigate_to_kemet_page()
        time.sleep(2)
        emi_rfi_filters.accept_cookies()
        emi_rfi_filters.hover_over_the_products_main_nav()
        emi_rfi_filters.hover_over_the_emc_sub_nav()
        emi_rfi_filters.click_on_emi_rfi_filters_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/emi-rfi-filters.html" == emi_rfi_filters.get_current_url()), \
            "This is not the EMI/RFI Filters page!"
        assert emi_rfi_filters.browse_tab_is_displayed()
        assert emi_rfi_filters.datasheets_tab_is_displayed()
        if emi_rfi_filters.emi_rfi_filters_category_slick_list_is_displayed:
            if emi_rfi_filters.all_emi_rfi_filters_displayed():
                time.sleep(2)
                emi_rfi_filters_slick_list_item_number = emi_rfi_filters.get_emi_rfi_filters_slick_list_items_count()
                print("\nEMI/RFI Filters Sub Categories:")
                for i in range(2, emi_rfi_filters_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = emi_rfi_filters.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All EMI/RFI Filters tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
