import time

import pytest
from selenium.webdriver.common.by import By

from pages.emc_category_pages import dc_chokes_page
from tests import config


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
                print("\nDC Chokes Sub Categories:")
                displayed_category_tiles_elems_title = dc_chokes.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_dc_chokes_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All DC Chokes tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
