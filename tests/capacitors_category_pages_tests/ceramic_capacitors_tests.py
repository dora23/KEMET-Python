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
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter products based on Style
    def test_select_filter_from_style_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter products based on Capacitance
    def test_select_filter_from_capacitance_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter products based on Capacitance Tolerance
    def test_select_filter_from_capacitance_tolerance_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter products based on Voltage AC
    def test_select_filter_from_voltage_ac_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter products based on Voltage DC
    def test_select_filter_from_voltage_dc_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter products based on Temperature Range
    def test_select_filter_from_temperature_range_drop_down_menu(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
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

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # See All Filters section
    def test_see_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        print('All Filters:')
        number_of_filter_menus = ceramic.get_filter_menus_count()
        for i in range(2, number_of_filter_menus + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(" + str(
                           i) + ") > a"}
            filter_menus = ceramic.find_items(locator)
            print(filter_menus.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on Temperature Coefficient
    def test_temperature_coefficient_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.click_on_temperature_coefficient_filter_menu()
        time.sleep(2)
        ceramic.scroll_to_temperature_coefficient_filter_menu()

        selected_temperature_coefficient_filter = "C0G"

        temperature_coefficient_filter_number = ceramic.get_temperature_coefficient_filters_count()
        for i in range(1, temperature_coefficient_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(9) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            temperature_coefficient_filter = ceramic.find_items(locator)
            if temperature_coefficient_filter.text == selected_temperature_coefficient_filter:
                temperature_coefficient_filter.click()
                time.sleep(2)
                ceramic.click_on_close_all_filters_section()
                time.sleep(2)
                assert 'Temperature Coefficient: ' + selected_temperature_coefficient_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on RoHS
    def test_rohs_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.click_on_rohs_filter_menu()
        time.sleep(2)
        ceramic.scroll_to_rohs_filter_menu()

        selected_rohs_filter = "With Exemptions"

        rohs_filter_number = ceramic.get_rohs_filters_count()
        for i in range(1, rohs_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(10) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            rohs_filter = ceramic.find_items(locator)
            if rohs_filter.text == selected_rohs_filter:
                rohs_filter.click()
                time.sleep(2)
                ceramic.click_on_close_all_filters_section()
                time.sleep(2)
                assert 'RoHS: ' + selected_rohs_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)
        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on Termination
    def test_termination_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.click_on_termination_filter_menu()
        time.sleep(2)
        ceramic.scroll_to_termination_filter_menu()

        selected_termination_filter = "Gold"

        termination_filter_number = ceramic.get_termination_filters_count()
        for i in range(1, termination_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(11) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            termination_filter = ceramic.find_items(locator)
            if termination_filter.text == selected_termination_filter:
                termination_filter.click()
                time.sleep(2)
                ceramic.click_on_close_all_filters_section()
                time.sleep(2)
                assert 'Termination: ' + selected_termination_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on AEC-Q200
    def test_aec_q200_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.click_on_aec_q200_filter_menu()
        time.sleep(2)
        ceramic.scroll_to_aec_q200_filter_menu()

        selected_aec_q200_filter = "No"

        aec_q200_filter_number = ceramic.get_aec_q200_filters_count()
        for i in range(1, aec_q200_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(12) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            aec_q200_filter = ceramic.find_items(locator)
            if aec_q200_filter.text == selected_aec_q200_filter:
                aec_q200_filter.click()
                time.sleep(2)
                ceramic.click_on_close_all_filters_section()
                time.sleep(2)
                assert 'AEC-Q200: ' + selected_aec_q200_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on Packaging
    def test_packaging_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.click_on_packaging_filter_menu()
        time.sleep(2)
        ceramic.scroll_to_packaging_filter_menu()

        selected_packaging_filter = "Ammo, H = 16.5mm, Component Pitch = 12.7mm"

        packaging_filter_number = ceramic.get_packaging_filters_count()
        for i in range(1, packaging_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(13) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            packaging_filter = ceramic.find_items(locator)
            if packaging_filter.text == selected_packaging_filter:
                packaging_filter.click()
                time.sleep(2)
                ceramic.click_on_close_all_filters_section()
                time.sleep(2)
                assert 'Packaging: ' + selected_packaging_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on K-SIM Modeling
    def test_ksim_modeling_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.click_on_ksim_modeling_filter_menu()
        time.sleep(2)
        ceramic.scroll_to_ksim_modeling_filter_menu()

        selected_ksim_modeling_filter = "Yes"

        ksim_modeling_filter_number = ceramic.get_ksim_modeling_filters_count()
        for i in range(1, ksim_modeling_filter_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(14) > div > ul > li:nth-child(" + str(
                           i) + ") > label > span"}
            ksim_modeling_filter = ceramic.find_items(locator)
            if ksim_modeling_filter.text == selected_ksim_modeling_filter:
                ksim_modeling_filter.click()
                time.sleep(2)
                ceramic.click_on_close_all_filters_section()
                time.sleep(2)
                assert 'K-SIM Modeling: ' + selected_ksim_modeling_filter == ceramic.get_selected_filter_text()
                ceramic.clear_selected_filter_text()
                time.sleep(2)

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for j in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           j) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------

    # Filter based on a searched word
    def test_searched_filter_from_all_filters_section(self, ceramic):
        ceramic.navigate_to_kemet_page()
        time.sleep(2)
        ceramic.accept_cookies()
        ceramic.hover_over_the_products_main_nav()
        ceramic.hover_over_the_capacitors_sub_nav()
        ceramic.click_on_ceramic_category()
        time.sleep(10)
        if ceramic.feedback_window_is_displayed():
            ceramic.close_feedback_window()
        time.sleep(2)

        ceramic.click_on_see_all_filters_button()
        time.sleep(2)
        ceramic.scroll_to_search_container()
        time.sleep(2)

        searched_word = "27 pF"

        ceramic.click_in_the_search_field()
        ceramic.search_for_a_word(searched_word)
        time.sleep(2)
        ceramic.click_on_the_show_results_button()
        time.sleep(2)
        assert 'Text Query: ' + searched_word == ceramic.get_selected_filter_text()

        print("\nFirst 20 Product Results:")
        product_results_number = ceramic.get_product_results_count()
        for i in range(1, product_results_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.browse-by__results-pinned-table > table > tbody > tr:nth-child(" + str(
                           i) + ") > td > div > div.browse-by__result-card-info-section > div.browse-by__result-card-description-wrapper > a"}
            products = ceramic.find_items(locator)
            print(products.text)

    # --------------------------------------------------------------------------------------------------
