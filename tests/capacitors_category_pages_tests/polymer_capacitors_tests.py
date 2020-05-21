import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import polymer_capacitor_page
from tests import config


class TestPolymerCapacitorsPage:
    @pytest.fixture()
    def polymer(self, driver):
        return polymer_capacitor_page.PolymerCapacitorsPage(driver)

    # Test Polymer Capacitor Slick Nav
    def test_polymer_sub_categories(self, polymer):
        polymer.navigate_to_kemet_page()
        time.sleep(2)
        polymer.accept_cookies()
        polymer.hover_over_the_products_main_nav()
        polymer.hover_over_the_capacitors_sub_nav()
        polymer.click_on_polymer_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/polymer.html" == polymer.get_current_url()), \
            "This is not the Polymer Capacitor page!"
        if polymer.polymer_category_slick_list_is_displayed:
            if polymer.all_polymer_displayed():
                print("\nPolymer Capacitors Sub Categories:")
                displayed_category_tiles_elems_title = polymer.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_polymer_capacitor_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Polymer Capacitors tab is not displayed")
        else:
            print("The Slick list is not displayed")
