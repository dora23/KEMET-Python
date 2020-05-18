import time

import pytest
from selenium.webdriver.common.by import By

from pages import products_section


class TestProductsMenu():
    @pytest.fixture()
    def products(self, driver):
        return products_section.ProductsSection(driver)

    # Print all product categories
    def test_products_nav_menu(self, products):
        products.navigate_to_kemet_page()
        time.sleep(2)
        products.accept_cookies()
        products.hover_over_the_products_main_nav()
        time.sleep(2)

        number_of_products_sub_nav_items = products.get_products_sub_nav_items_count()
        print("\nPRODUCTS:")
        for i in range(1, number_of_products_sub_nav_items + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#subNav_1 > div.header__sub-nav-content.header__sub-nav-content--products > ul > li:nth-child(" + str(
                           i) + ") > a"}
            product_nav_item_title = products.find_items(locator)
            print("\n" + product_nav_item_title.text)
    # -----------------------------------------------------------------

    # Print all the sub categories for the the CAPACITOR product category
    def test_capacitors_sub_nav_menu(self, products):
        products.navigate_to_kemet_page()
        time.sleep(2)
        products.accept_cookies()
        products.hover_over_the_products_main_nav()
        products.hover_over_the_capacitors_sub_nav()
        time.sleep(2)

        number_of_capacitors_items = products.get_capacitors_items_count()
        print("\nCAPACITORS Categories:")
        for i in range(1, number_of_capacitors_items + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(" + str(
                           i) + ") > a > div > span"}
            capacitors_sub_items_name = products.find_items(locator)
            print(capacitors_sub_items_name.text)
    # -----------------------------------------------------------------

    # Print all the sub categories for the the EMC product category
    def test_emc_sub_nav_menu(self, products):
        products.navigate_to_kemet_page()
        time.sleep(2)
        products.accept_cookies()
        products.hover_over_the_products_main_nav()
        products.hover_over_the_emc_sub_nav()
        time.sleep(2)

        number_of_emc_items = products.get_emc_items_count()
        print("\nEMC Categories:")
        for i in range(1, number_of_emc_items + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#subSubNav_2 > div.header__sub-nav-content > ul > li:nth-child(" + str(
                           i) + ") > a > div > span"}
            emc_sub_items_name = products.find_items(locator)
            print(emc_sub_items_name.text)
    # -----------------------------------------------------------------
