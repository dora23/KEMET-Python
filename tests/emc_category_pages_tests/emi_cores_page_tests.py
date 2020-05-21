import time

import pytest
from selenium.webdriver.common.by import By

from pages.emc_category_pages import emi_cores_page
from tests import config


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
                print("\nEMI Cores Sub Categories:")
                displayed_category_tiles_elems_title = emi_cores.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_emi_cores_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All EMI Cores tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
