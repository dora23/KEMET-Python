import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import polymer_capacitor_page


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
                polymer_slick_list_item_number = polymer.get_polymer_slick_list_items_count()
                print("\nPolymer Capacitors Sub Categories:")
                for i in range(2, polymer_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = polymer.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Polymer Capacitors tab is not displayed")
        else:
            print("The Slick list is not displayed")
