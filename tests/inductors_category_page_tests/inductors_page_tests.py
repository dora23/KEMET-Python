import time

import pytest

from pages.inductors_category_page import inductors_page
from tests import config


class TestInductorsPage:
    @pytest.fixture()
    def inductors(self, driver):
        return inductors_page.InductorsPage(driver)

    def test_inductors_sub_categories(self, inductors):
        inductors.navigate_to_kemet_page()
        time.sleep(2)
        inductors.accept_cookies()
        inductors.hover_over_the_products_main_nav()
        inductors.click_on_the_inductors_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/inductors.html" == inductors.get_current_url()), \
            "This is not the Inductors page!"
        assert inductors.browse_tab_is_displayed()
        assert inductors.datasheets_tab_is_displayed()
        if inductors.inductors_category_slick_list_is_displayed:
            if inductors.all_inductors_displayed():
                time.sleep(2)
                print('\nInductors Sub Categories:')
                displayed_category_tiles_elems_title = inductors.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_inductors_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Inductors tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
