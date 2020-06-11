from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class CeramicCapacitorsPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    capacitors_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_1-link'}
    browse_by_title = {"by": By.CSS_SELECTOR,
                       "value": '#category-browse-by > div > div > div.browse-by__header.grid-x > div > h3'}
    ceramic_category = {"by": By.CSS_SELECTOR,
                        "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(1) > a'}
    ceramic_page_slick_list = {"by": By.CSS_SELECTOR, "value": '#panel1c > div.category-tiles > div > div > div'}
    slick_list_right_arrow = {"by": By.CSS_SELECTOR, "value": 'span.icon-chevron-right.slick-arrow'}
    all_ceramic_sub_category = {"by": By.CSS_SELECTOR,
                                "value": 'div.category-tiles__item.category-tiles__item--text.active.slick-slide.slick-current.slick-active > a'}
    series_filter = {"by": By.CSS_SELECTOR,
                     "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(1)'}
    series_filter_menu = {"by": By.CSS_SELECTOR,
                          "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(1) > div'}
    style_filter = {"by": By.CSS_SELECTOR,
                    "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(2)'}
    style_filter_menu = {"by": By.CSS_SELECTOR,
                         "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(2) > div'}
    capacitance_filter = {"by": By.CSS_SELECTOR,
                          "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(3)'}
    capacitance_filter_menu = {"by": By.CSS_SELECTOR,
                               "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(3) > div'}
    capacitance_tolerance_filter = {"by": By.CSS_SELECTOR,
                                    "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(4)'}
    capacitance_tolerance_filter_menu = {"by": By.CSS_SELECTOR,
                                         "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(4) > div'}
    voltage_ac_filter = {"by": By.CSS_SELECTOR,
                         "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(5)'}
    voltage_ac_filter_menu = {"by": By.CSS_SELECTOR,
                              "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(5) > div'}
    voltage_dc_filter = {"by": By.CSS_SELECTOR,
                         "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(6)'}
    voltage_dc_filter_menu = {"by": By.CSS_SELECTOR,
                              "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(6) > div'}
    temperature_range_filter = {"by": By.CSS_SELECTOR,
                                "value": '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(7)'}
    temperature_range_filter_menu = {"by": By.CSS_SELECTOR,
                                     "value": '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(7) > div'}
    see_all_filters_button = {"by": By.CSS_SELECTOR,
                              "value": '#category-browse-by > div > div > div:nth-child(2) > div > a'}
    selected_filter = {"by": By.CSS_SELECTOR,
                       "value": 'div.filters-section__active-filters.show-for-large > ul > li:nth-child(1) > a'}
    close_all_filters_button = {"by": By.CSS_SELECTOR,
                                "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-close-wrapper > a'}
    temperature_coefficient_filter = {"by": By.CSS_SELECTOR,
                                      "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(9)'}
    temperature_coefficient_menu = {"by": By.CSS_SELECTOR,
                                    "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(9) > div'}
    rohs_filter = {"by": By.CSS_SELECTOR,
                   "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(10)'}
    rohs_menu = {"by": By.CSS_SELECTOR,
                 "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(10) > div'}
    termination_filter = {"by": By.CSS_SELECTOR,
                          "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(11)'}
    termination_menu = {"by": By.CSS_SELECTOR,
                        "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(11) > div'}
    aec_q200_filter = {"by": By.CSS_SELECTOR,
                       "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(12)'}
    aec_q200_menu = {"by": By.CSS_SELECTOR,
                     "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(12) > div'}
    packaging_filter = {"by": By.CSS_SELECTOR,
                        "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(13)'}
    packaging_menu = {"by": By.CSS_SELECTOR,
                      "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(13) > div'}
    ksim_modeling_filter = {"by": By.CSS_SELECTOR,
                            "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(14)'}
    ksim_modeling_menu = {"by": By.CSS_SELECTOR,
                          "value": '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(14) > div'}
    search_container = {"by": By.CLASS_NAME, "value": 'filters-section__search-container'}
    search_field = {"by": By.CSS_SELECTOR, "value": 'div.filters-section__search-container > input'}
    show_results_button = {"by": By.CSS_SELECTOR, "value": 'div.filters-section__all-filters-footer > a'}
    feedback_window = {"by": By.CSS_SELECTOR, "value": '#leadinModal-content-wrapper-833502 > div > div'}
    close_feedback_window_button = {"by": By.CSS_SELECTOR,
                                    "value": '#leadinModal-833502 > div.leadinModal-content > button'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    def get_current_url(self):
        return self._get_current_url()

    def hover_over_the_products_main_nav(self):
        self._hover(self.products_tab)

    def hover_over_the_capacitors_sub_nav(self):
        self._hover(self.capacitors_sub_nav_tab)

    def get_browse_by_title_text(self):
        return self._get_text(self.browse_by_title)

    def click_on_ceramic_category(self):
        self._click(self.ceramic_category)

    def ceramic_category_slick_list_is_displayed(self):
        return self._is_displayed(self.ceramic_page_slick_list)

    def all_ceramic_displayed(self):
        return self._is_displayed(self.all_ceramic_sub_category)

    def click_on_slick_list_right_arrow(self):
        self._click(self.slick_list_right_arrow)

    def get_displayed_subcategory_tiles_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            'div.category-tiles__item > a > div.category-tiles__item-info > span')
        return _elems

    def get_selected_filter_text(self):
        return self._get_text(self.selected_filter)

    def clear_selected_filter_text(self):
        self._click(self.selected_filter)

    def click_on_show_results_button(self):
        self._click(self.show_results_button)

    def click_on_close_all_filters_section(self):
        self._click(self.close_all_filters_button)

    def feedback_window_is_displayed(self):
        return self._is_displayed(self.feedback_window)

    def close_feedback_window(self):
        self._click(self.close_feedback_window_button)

    # Series Filter drop down menu
    def click_on_series_filter(self):
        self._click(self.series_filter)

    def scroll_to_series_filter_menu(self):
        self._scroll_to_element(self.series_filter_menu)

    def get_series_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(1) > div > ul > li')
        return elems

    def get_series_filters_count(self):
        return len(self.get_series_filters())

    # --------------------------------------------------------------------------------------

    # Style Filter drop down menu
    def click_on_style_filter(self):
        self._click(self.style_filter)

    def scroll_to_style_filter_menu(self):
        self._scroll_to_element(self.style_filter_menu)

    def get_style_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div > div:nth-child(2) > div > ul > li')
        return elems

    def get_style_filters_count(self):
        return len(self.get_style_filters())

    # --------------------------------------------------------------------------------------

    # Capacitance Filter drop down menu
    def click_on_capacitance_filter(self):
        self._click(self.capacitance_filter)

    def scroll_to_capacitance_filter_menu(self):
        self._scroll_to_element(self.capacitance_filter_menu)

    def get_capacitance_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(3) > div > ul > li')
        return elems

    def get_capacitance_filters_count(self):
        return len(self.get_capacitance_filters())

    # --------------------------------------------------------------------------------------

    # Capacitance Tolerance Filter drop down menu
    def click_on_capacitance_tolerance_filter(self):
        self._click(self.capacitance_tolerance_filter)

    def scroll_to_capacitance_tolerance_filter_menu(self):
        self._scroll_to_element(self.capacitance_tolerance_filter_menu)

    def get_capacitance_tolerance_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(4) > div > ul > li')
        return elems

    def get_capacitance_tolerance_filters_count(self):
        return len(self.get_capacitance_tolerance_filters())

    # --------------------------------------------------------------------------------------

    # Voltage AC drop down menu
    def click_on_voltage_ac_filter(self):
        self._click(self.voltage_ac_filter)

    def scroll_to_voltage_ac_filter_menu(self):
        self._scroll_to_element(self.voltage_ac_filter_menu)

    def get_voltage_ac_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(5) > div > ul > li')
        return elems

    def get_voltage_ac_filters_count(self):
        return len(self.get_voltage_ac_filters())

    # --------------------------------------------------------------------------------------

    # Voltage DC drop down menu
    def click_on_voltage_dc_filter(self):
        self._click(self.voltage_dc_filter)

    def scroll_to_voltage_dc_filter_menu(self):
        self._scroll_to_element(self.voltage_dc_filter_menu)

    def get_voltage_dc_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(6) > div > ul > li')
        return elems

    def get_voltage_dc_filters_count(self):
        return len(self.get_voltage_dc_filters())

    # --------------------------------------------------------------------------------------

    # Temperature Range drop down menu
    def click_on_temperature_range_filter(self):
        self._click(self.temperature_range_filter)

    def scroll_to_temperature_range_filter_menu(self):
        self._scroll_to_element(self.temperature_range_filter_menu)

    def get_temperature_range_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#category-browse-by > div > div > div:nth-child(2) > div.filters-section > div:nth-child(7) > div > ul > li')
        return elems

    def get_temperature_range_filters_count(self):
        return len(self.get_temperature_range_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section
    def click_on_see_all_filters_button(self):
        self._click(self.see_all_filters_button)

    def get_filter_menus(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div')
        return elems

    def get_filter_menus_count(self):
        return len(self.get_filter_menus())

    # --------------------------------------------------------------------------------------

    # See All Filters section - Temperature Coefficient filter
    def click_on_temperature_coefficient_filter_menu(self):
        self._click(self.temperature_coefficient_filter)

    def scroll_to_temperature_coefficient_filter_menu(self):
        self._scroll_to_element(self.temperature_coefficient_menu)

    def get_temperature_coefficient_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(9) > div > ul > li')
        return elems

    def get_temperature_coefficient_filters_count(self):
        return len(self.get_temperature_coefficient_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section - RoHS filter
    def click_on_rohs_filter_menu(self):
        self._click(self.rohs_filter)

    def scroll_to_rohs_filter_menu(self):
        self._scroll_to_element(self.rohs_menu)

    def get_rohs_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(10) > div > ul > li')
        return elems

    def get_rohs_filters_count(self):
        return len(self.get_rohs_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section - Termination filter
    def click_on_termination_filter_menu(self):
        self._click(self.termination_filter)

    def scroll_to_termination_filter_menu(self):
        self._scroll_to_element(self.termination_menu)

    def get_termination_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(11) > div > ul > li')
        return elems

    def get_termination_filters_count(self):
        return len(self.get_termination_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section - AEC-Q200 filter
    def click_on_aec_q200_filter_menu(self):
        self._click(self.aec_q200_filter)

    def scroll_to_aec_q200_filter_menu(self):
        self._scroll_to_element(self.aec_q200_menu)

    def get_aec_q200_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(12) > div > ul > li')
        return elems

    def get_aec_q200_filters_count(self):
        return len(self.get_aec_q200_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section - Packaging filter
    def click_on_packaging_filter_menu(self):
        self._click(self.packaging_filter)

    def scroll_to_packaging_filter_menu(self):
        self._scroll_to_element(self.packaging_menu)

    def get_packaging_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(13) > div > ul > li')
        return elems

    def get_packaging_filters_count(self):
        return len(self.get_packaging_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section - K-SIM Modeling filter
    def click_on_ksim_modeling_filter_menu(self):
        self._click(self.ksim_modeling_filter)

    def scroll_to_ksim_modeling_filter_menu(self):
        self._scroll_to_element(self.ksim_modeling_menu)

    def get_ksim_modeling_filters(self):
        elems = self.driver.find_elements_by_css_selector(
            '#specifications-browse-by__all-filters > div.filters-section__all-filters-body > div:nth-child(14) > div > ul > li')
        return elems

    def get_ksim_modeling_filters_count(self):
        return len(self.get_ksim_modeling_filters())

    # --------------------------------------------------------------------------------------

    # See All Filters section - SEARCH
    def scroll_to_search_container(self):
        self._scroll_to_element(self.search_container)

    def click_in_the_search_field(self):
        self._click(self.search_field)

    def search_for_a_word(self, word):
        self._type(self.search_field, word)

    def click_on_the_show_results_button(self):
        self._click(self.show_results_button)

    # --------------------------------------------------------------------------------------

    # Product Results section
    def get_product_results(self):
        elems = self.driver.find_elements_by_css_selector('div.browse-by__results-pinned-table > table > tbody > tr')
        return elems

    def get_product_results_count(self):
        return len(self.get_product_results())

    # --------------------------------------------------------------------------------------
