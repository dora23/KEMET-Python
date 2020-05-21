import time

import pytest

from pages.varistors_category_page import varistors_page
from tests import config


class TestVaristorsPage:
    @pytest.fixture()
    def varistors(self, driver):
        return varistors_page.VaristorsPage(driver)

    def test_relays_sub_categories(self, varistors):
        varistors.navigate_to_kemet_page()
        time.sleep(2)
        varistors.accept_cookies()
        varistors.hover_over_the_products_main_nav()
        varistors.click_on_the_varistors_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/varistors.html" == varistors.get_current_url()), \
            "This is not the Varistors page!"
        assert varistors.browse_tab_is_displayed()
        assert varistors.datasheets_tab_is_displayed()
        if varistors.varistors_category_slick_list_is_displayed:
            if varistors.all_varistors_devices_displayed():
                time.sleep(2)
                print('\nVaristors Categories:')
                displayed_category_tiles_elems_title = varistors.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_varistors_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Varistors tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
