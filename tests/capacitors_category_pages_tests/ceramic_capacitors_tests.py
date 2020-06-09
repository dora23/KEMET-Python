import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import ceramic_capacitor_page
from tests import config


class TestCeramicCapacitorPage:
    @pytest.fixture()
    def ceramic(self, driver):
        return ceramic_capacitor_page.CeramicCapacitorsPage(driver)

    # Test Ceramic Capacitor Slick Nav
    def test_ceramic_sub_categories(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/ceramic.html" == ceramic.get_current_url()), \
            "This is not the Ceramic Capacitor page!"
        if ceramic.ceramic_category_slick_list_is_displayed:
            if ceramic.all_ceramic_displayed():
                ceramic.click_on_slick_list_right_arrow()
                time.sleep(2)
                print("\nCeramic Capacitors Sub Categories:")
                displayed_category_tiles_elems_title = ceramic.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_ceramic_capacitor_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All Ceramic tab is not displayed")
        else:
            print("The Slick list is not displayed")
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Series
    def test_select_filter_from_series_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_series_filter()
        time.sleep(2)
        ceramic.scroll_to_series_filter_menu()
        selected_series_filter = "C900AC SFTY X1-440 Y2-300"
        series_filter_number = ceramic.get_series_filters_count()
        for i in range(1, series_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(1) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            series_filter = ceramic.find_items(locator)
            if series_filter.text == selected_series_filter:
                series_filter.click()
                time.sleep(2)
                ceramic.click_on_series_filter()
                time.sleep(2)
                assert 'Series: ' + selected_series_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Style
    def test_select_filter_from_style_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_style_filter()
        time.sleep(2)
        ceramic.scroll_to_style_filter_menu()
        selected_style_filter = "Stacked Chip"
        style_filter_number = ceramic.get_style_filters_count()
        for i in range(1, style_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(2) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            style_filter = ceramic.find_items(locator)
            if style_filter.text == selected_style_filter:
                style_filter.click()
                time.sleep(2)
                ceramic.click_on_style_filter()
                time.sleep(2)
                assert 'Style: ' + selected_style_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Capacitance
    def test_select_filter_from_capacitance_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_capacitance_filter()
        time.sleep(2)
        ceramic.scroll_to_capacitance_filter_menu()
        selected_capacitance_filter = "4.4 pF"
        capacitance_filter_number = ceramic.get_capacitance_filters_count()
        for i in range(1, capacitance_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(3) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            capacitance_filter = ceramic.find_items(locator)
            if capacitance_filter.text == selected_capacitance_filter:
                capacitance_filter.click()
                time.sleep(2)
                ceramic.click_on_capacitance_filter()
                time.sleep(2)
                assert 'Capacitance: ' + selected_capacitance_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Capacitance Tolerance
    def test_select_filter_from_capacitance_tolerance_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_capacitance_tolerance_filter()
        time.sleep(2)
        ceramic.scroll_to_capacitance_tolerance_filter_menu()
        selected_capacitance_tolerance_filter = "-20/+80%"
        capacitance_tolerance_filter_number = ceramic.get_capacitance_tolerance_filters_count()
        for i in range(1, capacitance_tolerance_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(4) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            capacitance_tolerance_filter = ceramic.find_items(locator)
            if capacitance_tolerance_filter.text == selected_capacitance_tolerance_filter:
                capacitance_tolerance_filter.click()
                time.sleep(2)
                ceramic.click_on_capacitance_tolerance_filter()
                time.sleep(2)
                assert 'Capacitance Tolerance: ' + selected_capacitance_tolerance_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Voltage AC
    def test_select_filter_from_voltage_ac_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_voltage_ac_filter()
        time.sleep(2)
        ceramic.scroll_to_voltage_ac_filter_menu()
        selected_voltage_ac_filter = "400 VAC"
        voltage_ac_filter_number = ceramic.get_voltage_ac_filters_count()
        for i in range(1, voltage_ac_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(5) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            voltage_ac_filter = ceramic.find_items(locator)
            if voltage_ac_filter.text == selected_voltage_ac_filter:
                voltage_ac_filter.click()
                time.sleep(2)
                ceramic.click_on_voltage_ac_filter()
                time.sleep(2)
                assert 'Voltage AC: ' + selected_voltage_ac_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Voltage DC
    def test_select_filter_from_voltage_dc_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_voltage_dc_filter()
        time.sleep(2)
        ceramic.scroll_to_voltage_dc_filter_menu()
        selected_voltage_ac_filter = "25 VDC"
        voltage_dc_filter_number = ceramic.get_voltage_dc_filters_count()
        for i in range(1, voltage_dc_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(6) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            voltage_dc_filter = ceramic.find_items(locator)
            if voltage_dc_filter.text == selected_voltage_ac_filter:
                voltage_dc_filter.click()
                time.sleep(2)
                ceramic.click_on_voltage_dc_filter()
                time.sleep(2)
                assert 'Voltage DC: ' + selected_voltage_ac_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------

    # Filter products based on Temperature Range
    def test_select_filter_from_temperature_range_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(2)

        ceramic.click_on_temperature_range_filter()
        time.sleep(2)
        ceramic.scroll_to_temperature_range_filter_menu()
        selected_temperature_range_filter = "-40/+125°C"
        temperature_range_filter_number = ceramic.get_temperature_range_filters_count()
        for i in range(1, temperature_range_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(7) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            temperature_range_filter = ceramic.find_items(locator)
            if temperature_range_filter.text == selected_temperature_range_filter:
                temperature_range_filter.click()
                time.sleep(2)
                ceramic.click_on_voltage_ac_filter()
                time.sleep(2)
                assert 'Temperature Range: ' + selected_temperature_range_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
    # --------------------------------------------------------------------------------------------------
