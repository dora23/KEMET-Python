import time

import pytest
from selenium.webdriver.common.by import By

from pages.emc_category_pages import emi_rfi_filters_page
from tests import config


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
                print("\nEMI/RFI Filters Sub Categories:")
                displayed_category_tiles_elems_title = emi_rfi_filters.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_emi_rfi_filters_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All EMI/RFI Filters tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
