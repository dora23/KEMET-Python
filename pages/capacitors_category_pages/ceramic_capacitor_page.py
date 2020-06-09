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

    def click_on_see_all_filters_button(self):
        self._click(self.see_all_filters_button)
