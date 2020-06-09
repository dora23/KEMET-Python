import time

import pytest

from pages.engineering_kits_category_page import engineering_kits_page
from tests import config


class TestEngineeringKitsPage:
    @pytest.fixture()
    def eng_kits(self, driver):
        return engineering_kits_page.EngineeringKitsPage(driver)

    def test_engineering_kits_sub_categories(self, eng_kits):
        eng_kits.navigate_to_kemet_page()
        time.sleep(2)
        eng_kits.accept_cookies()
        eng_kits.hover_over_the_products_main_nav()
        eng_kits.click_on_the_engineering_kits_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/engineering-kits.html" == eng_kits.get_current_url()), \
            "This is not the Engineering Kits page!"
        assert eng_kits.browse_tab_is_displayed()
        if eng_kits.engineering_kits_category_slick_list_is_displayed:
            if eng_kits.all_engineering_kits_displayed():
                time.sleep(2)
                print('\nEngineering Kits Categories:')
                displayed_category_tiles_elems_title = eng_kits.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_engineering_kits_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
                    if eng_kits.slick_list_right_arrow_is_displayed():
                        eng_kits.click_on_slick_list_right_arrow()
                    else:
                        category_tiles_elems.append(title.text)
            else:
                print("The All Engineering Kits tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------
# TODO: find a solution for this test to pass
