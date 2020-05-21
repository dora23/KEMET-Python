import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import tantalum_capacitor_page
from tests import config


class TestTantalumCapacitorsPage:
    @pytest.fixture()
    def tantalum(self, driver):
        return tantalum_capacitor_page.TantalumCapacitorsPage(driver)

    # Test Tantalum Capacitor Slick Nav
    def test_ceramic_sub_categories(self, tantalum):
        tantalum.navigate_to_kemet_page()
        time.sleep(2)
        tantalum.accept_cookies()
        tantalum.hover_over_the_products_main_nav()
        tantalum.hover_over_the_capacitors_sub_nav()
        tantalum.click_on_tantalum_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/tantalum.html" == tantalum.get_current_url()), \
            "This is not the Tantalum Capacitor page!"
        if tantalum.tantalum_category_slick_list_is_displayed:
            if tantalum.all_tantalum_displayed():
                print("\nTantalum Capacitors Sub Categories:")
                displayed_category_tiles_elems_title = tantalum.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_tantalum_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Tantalum tab is not displayed")
        else:
            print("The Slick list is not displayed")