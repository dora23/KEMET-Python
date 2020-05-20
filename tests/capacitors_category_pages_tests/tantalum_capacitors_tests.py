import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import tantalum_capacitor_page


class TestTantalumCapacitorsPage:
    @pytest.fixture()
    def tantalum(self, driver):
        return tantalum_capacitor_page.TantalumCapacitorsPage(driver)

    # Test Tantalum Capacitor Slick Nav
    def test_ceramic_sub_categories(self, tantalum):
        tantalum.navigate_to_kemet_page()
        time.sleep(2)
        tantalum.accept_cookies()
        tantalum.hover_over_the_products_main_nav()
        tantalum.hover_over_the_capacitors_sub_nav()
        tantalum.click_on_tantalum_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/tantalum.html" == tantalum.get_current_url()), \
            "This is not the Tantalum Capacitor page!"
        if tantalum.tantalum_category_slick_list_is_displayed:
            if tantalum.all_tantalum_displayed():
                tantalum_slick_list_item_number = tantalum.get_tantalum_slick_list_items_count()
                print("\nTantalum Capacitors Sub Categories:")
                for i in range(2, tantalum_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = tantalum.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")