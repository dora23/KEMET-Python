import time

import pytest

from pages.relays_category_page import relays_page
from tests import config


class TestRelaysPage:
    @pytest.fixture()
    def relays(self, driver):
        return relays_page.RelaysPage(driver)

    def test_relays_sub_categories(self, relays):
        relays.navigate_to_kemet_page()
        time.sleep(2)
        relays.accept_cookies()
        relays.hover_over_the_products_main_nav()
        relays.click_on_the_relays_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/relays.html" == relays.get_current_url()), \
            "This is not the Relays page!"
        assert relays.browse_tab_is_displayed()
        assert relays.datasheets_tab_is_displayed()
        if relays.relays_category_slick_list_is_displayed:
            if relays.all_relays_devices_displayed():
                time.sleep(2)
                print('\nRelays Categories:')
                displayed_category_tiles_elems_title = relays.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_relays_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Relays tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
