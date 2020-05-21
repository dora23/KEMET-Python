import time

import pytest

from pages.piezoelectric_devices_category_page import piezoelectric_devices_page
from tests import config


class TestPiezoelectricDevicesPage:
    @pytest.fixture()
    def piezoelectric(self, driver):
        return piezoelectric_devices_page.PiezoelectricDevicesPage(driver)

    def test_piezoelectric_devices_sub_categories(self, piezoelectric):
        piezoelectric.navigate_to_kemet_page()
        time.sleep(2)
        piezoelectric.accept_cookies()
        piezoelectric.hover_over_the_products_main_nav()
        piezoelectric.click_on_the_piezoelectric_devices_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/piezoelectric-devices.html" == piezoelectric.get_current_url()), \
            "This is not the Piezoelectric Devices page!"
        assert piezoelectric.browse_tab_is_displayed()
        assert piezoelectric.datasheets_tab_is_displayed()
        if piezoelectric.piezoelectric_devices_category_slick_list_is_displayed:
            if piezoelectric.all_piezoelectric_devices_displayed():
                time.sleep(2)
                print('\nPiezoelectric Devices Sub Categories:')
                displayed_category_tiles_elems_title = piezoelectric.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_piezoelectric_devices_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Piezoelectric tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
