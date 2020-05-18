import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import aluminium_capacitors_page


class TestAluminiumCapacitorPage:
    @pytest.fixture()
    def aluminium(self, driver):
        return aluminium_capacitors_page.AluminiumCapacitorsPages(driver)

    # Test Ceramic Capacitor Slick Nav
    def test_ceramic_sub_categories(self, aluminium):
        aluminium.navigate_to_kemet_page()
        time.sleep(2)
        aluminium.accept_cookies()
        aluminium.hover_over_the_products_main_nav()
        aluminium.hover_over_the_capacitors_sub_nav()
        aluminium.click_on_aluminium_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/aluminum.html" == aluminium.get_current_url()), \
            "This is not the Ceramic Capacitor page!"
        if aluminium.aluminium_category_slick_list_is_displayed:
            if aluminium.all_aluminium_displayed():
                aluminium.click_on_slick_list_right_arrow()
                time.sleep(2)
                ceramic_slick_list_item_number = aluminium.get_aluminium_slick_list_items_count()
                print("\nCeramic Sub Categories:")
                for i in range(2, ceramic_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = aluminium.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------