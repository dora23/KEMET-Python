import time

import pytest
from selenium.webdriver.common.by import By

from pages.header_section import where_to_buy_nav_section


class TestWhereToBuy:
    @pytest.fixture()
    def where(self, driver):
        return where_to_buy_nav_section.WhereToBuySection(driver)

    # Navigate to Find A Distributor page and do some checks
    def test_find_a_distributor_page(self, where):
        where.navigate_to_kemet_page()
        time.sleep(2)
        where.accept_cookies()
        where.hover_over_where_to_buy()
        time.sleep(2)
        where.click_on_find_a_distributor()
        assert "https://www.kemet.com/en/us/where-to-buy/find-a-distributor.html" == where.get_current_url()

        number_of_global_distributors = where.get_global_distributors_items_count()
        print("\nGlobal Distributors:")
        for j in range(1, number_of_global_distributors + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.find-kemet-distributor__global-distributors > div > div:nth-child(" + str(
                           j) + ") > div >  div  > a"}
            global_distributor_item_title = where.find_items(locator)
            print(global_distributor_item_title.text)

        where.click_on_region_drop_down_menu()
        where.select_option_from_the_region_drop_down('EMEA')
        where.click_on_country_drop_down_menu()
        where.select_option_from_the_country_drop_down('Estonia')

        number_of_regional_distributors = where.get_regional_distributors_items_count()
        print("\nRegional Distributors:")
        for j in range(1, number_of_regional_distributors + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.find-kemet-distributor__regional-distributors > div > div:nth-child(" + str(
                           j) + ") > div > a"}
            regional_distributor_item_title = where.find_items(locator)
            print(regional_distributor_item_title.text)

    # --------------------------------------------------------------------------

    # Navigate to Find A Sales Representative page and do some checks
    def test_find_a_sales_reps_page_by_selecting_only_the_country(self, where):
        where.navigate_to_kemet_page()
        time.sleep(2)
        where.accept_cookies()
        where.hover_over_where_to_buy()
        time.sleep(2)
        where.click_on_find_a_sales_rep()
        assert "https://www.kemet.com/en/us/where-to-buy/find-a-sales-rep.html" == where.get_current_url()
        where.click_on_region_drop_down_menu_sales_rep()
        where.select_option_from_the_region_drop_down_sales_rep('United States')
        time.sleep(2)

        print("\nAll Sales Representatives:")
        number_of_all_sales_reps = where.get_sales_reps_items_count()
        if number_of_all_sales_reps != 0:
            for i in range(1, number_of_all_sales_reps + 1):
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.find-sales-representative__distributors > div > div > div:nth-child(" + str(
                               i) + ") > div.find-sales-representative__distributor-info > h4"}
                all_sales_reps = where.find_items(locator)
                print(all_sales_reps.text)
        else:
            print('The ALL Sales Reps section is empty!')

        where.select_kemet_sales_office_checkbox()
        time.sleep(2)
        print("\nKEMET Sales Office:")
        number_of_kemet_sales_reps = where.get_sales_reps_items_count()
        if number_of_kemet_sales_reps != 0:
            for i in range(1, number_of_kemet_sales_reps + 1):
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.find-sales-representative__distributors > div > div > div:nth-child(" + str(
                               i) + ") > div.find-sales-representative__distributor-info > h4"}
                kemet_sales_reps = where.find_items(locator)
                print(kemet_sales_reps.text)
        else:
            print('There are no KEMET Sales Offices!')

        where.select_manufacturers_rep_checkbox()
        time.sleep(2)
        print("\nManufacturer's Representative:")
        number_of_manufacturers_reps = where.get_sales_reps_items_count()
        if number_of_manufacturers_reps != 0:
            for i in range(1, number_of_manufacturers_reps + 1):
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.find-sales-representative__distributors > div > div > div:nth-child(" + str(
                               i) + ") > div.find-sales-representative__distributor-info > h4"}
                manufacturers_reps = where.find_items(locator)
                print(manufacturers_reps.text)
        else:
            print('There are no Manufacturers Representatives!')

    def test_find_a_sales_reps_page_by_selecting_country_and_state(self, where):
        where.navigate_to_kemet_page()
        time.sleep(2)
        where.accept_cookies()
        where.hover_over_where_to_buy()
        time.sleep(2)
        where.click_on_find_a_sales_rep()
        assert "https://www.kemet.com/en/us/where-to-buy/find-a-sales-rep.html" == where.get_current_url()

        where.click_on_region_drop_down_menu_sales_rep()
        where.select_option_from_the_region_drop_down_sales_rep('United States')
        time.sleep(2)
        where.click_on_country_drop_down_menu_sales_rep()
        where.select_option_from_the_country_drop_down_sales_rep('Iowa')

        print("\nAll Sales Representatives:")
        number_of_all_sales_reps = where.get_sales_reps_items_count()
        if number_of_all_sales_reps != 0:
            for i in range(1, number_of_all_sales_reps + 1):
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.find-sales-representative__distributors > div > div > div:nth-child(" + str(
                               i) + ") > div.find-sales-representative__distributor-info > h4"}
                all_sales_reps = where.find_items(locator)
                print(all_sales_reps.text)
        else:
            print('The ALL Sales Reps section is empty!')

        where.select_kemet_sales_office_checkbox()
        time.sleep(2)
        print("\nKEMET Sales Office:")
        number_of_kemet_sales_reps = where.get_sales_reps_items_count()
        if number_of_kemet_sales_reps != 0:
            for i in range(1, number_of_kemet_sales_reps + 1):
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.find-sales-representative__distributors > div > div > div:nth-child(" + str(
                               i) + ") > div.find-sales-representative__distributor-info > h4"}
                kemet_sales_reps = where.find_items(locator)
                print(kemet_sales_reps.text)
        else:
            print('There are no KEMET Sales Offices!')

        where.select_manufacturers_rep_checkbox()
        time.sleep(2)
        print("\nManufacturer's Representative:")
        number_of_manufacturers_reps = where.get_sales_reps_items_count()
        if number_of_manufacturers_reps != 0:
            for i in range(1, number_of_manufacturers_reps + 1):
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.find-sales-representative__distributors > div > div > div:nth-child(" + str(
                               i) + ") > div.find-sales-representative__distributor-info > h4"}
                manufacturers_reps = where.find_items(locator)
                print(manufacturers_reps.text)
        else:
            print('There are no Manufacturers Representatives!')
