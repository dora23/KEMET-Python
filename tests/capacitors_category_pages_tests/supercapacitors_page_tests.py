import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import supercapacitors_page
from tests import config


class TestSupercapacitorsPage:
    @pytest.fixture()
    def super(self, driver):
        return supercapacitors_page.SuperCapacitorsPage(driver)

    # Test Supercapacitors Slick Nav
    def test_supercapacitors_sub_categories(self, super):
        super.navigate_to_kemet_page()
        time.sleep(2)
        super.accept_cookies()
        super.hover_over_the_products_main_nav()
        super.hover_over_the_capacitors_sub_nav()
        super.click_on_supercapacitors_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/supercapacitors.html" == super.get_current_url()), \
            "This is not the Supercapacitor page!"
        if super.supercapacitors_category_slick_list_is_displayed:
            if super.all_supercapacitors_displayed():
                print("\nSupercapacitors Sub Categories:")
                displayed_category_tiles_elems_title = super.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_supercapacitors_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Supercapacitors tab is not displayed")
        else:
            print("The Slick list is not displayed")
