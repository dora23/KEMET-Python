import time

import pytest

from pages.sensors_category_page import sensors_page
from tests import config


class TestSensorsPage:
    @pytest.fixture()
    def sensors(self, driver):
        return sensors_page.SensorsPage(driver)

    def test_sensors_sub_categories(self, sensors):
        sensors.navigate_to_kemet_page()
        time.sleep(2)
        sensors.accept_cookies()
        sensors.hover_over_the_products_main_nav()
        sensors.click_on_the_sensors_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/sensors.html" == sensors.get_current_url()), \
            "This is not the Sensors page!"
        assert sensors.browse_tab_is_displayed()
        assert sensors.datasheets_tab_is_displayed()
        if sensors.sensors_category_slick_list_is_displayed:
            if sensors.all_sensors_displayed():
                time.sleep(2)
                print('\nSensors Sub Categories:')
                displayed_category_tiles_elems_title = sensors.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_sensors_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Sensors tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
