import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import aluminium_capacitor_page
from tests import config


class TestAluminiumCapacitorPage:
    @pytest.fixture()
    def aluminium(self, driver):
        return aluminium_capacitor_page.AluminiumCapacitorsPage(driver)

    # Test Aluminium Capacitor Slick Nav
    def test_aluminium_sub_categories(self, aluminium):
        aluminium.navigate_to_kemet_page()
        time.sleep(2)
        aluminium.accept_cookies()
        aluminium.hover_over_the_products_main_nav()
        aluminium.hover_over_the_capacitors_sub_nav()
        aluminium.click_on_aluminium_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/aluminum.html" == aluminium.get_current_url()), \
            "This is not the Aluminium Capacitor page!"
        if aluminium.aluminium_category_slick_list_is_displayed:
            if aluminium.all_aluminium_displayed():
                aluminium.click_on_slick_list_right_arrow()
                time.sleep(2)
                print("\nAluminium Capacitors Sub Categories:")
                displayed_category_tiles_elems_title = aluminium.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_aluminium_capacitor_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Aluminium tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
