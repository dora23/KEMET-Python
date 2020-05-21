import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import ceramic_capacitor_page
from tests import config


class TestCeramicCapacitorPage:
    @pytest.fixture()
    def ceramic(self, driver):
        return ceramic_capacitor_page.CeramicCapacitorsPage(driver)

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
                print("\nCeramic Capacitors Sub Categories:")
                displayed_category_tiles_elems_title = ceramic.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_ceramic_capacitor_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
