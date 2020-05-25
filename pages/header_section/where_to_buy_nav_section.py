from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class WhereToBuySection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    where_to_buy_tab = {"by": By.CSS_SELECTOR,
                        "value": 'ul.header__quick-utilities.show-for-xlarge > li:nth-child(2) > a'}
    find_a_distri = {"by": By.CSS_SELECTOR,
                     "value": 'ul.header__quick-utilities.show-for-xlarge > li:nth-child(2) > ul > li:nth-child(1) > a'}
    find_a_sales_rep = {"by": By.CSS_SELECTOR,
                        "value": 'ul.header__quick-utilities.show-for-xlarge > li:nth-child(2) > ul > li:nth-child(2) > a'}
    region_option_drop_down_menu_distri = {"by": By.CSS_SELECTOR,
                                           "value": '#find-kemet-distributor > div > div.find-kemet-distributor__filters > div > div > div > select'}
    country_option_drop_down_menu_distri = {"by": By.CSS_SELECTOR,
                                            "value": '#find-kemet-distributor > div > div.find-kemet-distributor__filters > div > div:nth-child(2) > div > select'}
    region_option_drop_down_menu_sales_rep = {"by": By.CSS_SELECTOR,
                                              "value": 'div.find-sales-representative__dropdown-list > div:nth-child(1) > div > select'}
    state_option_drop_down_menu_sales_rep = {"by": By.CSS_SELECTOR,
                                             "value": 'div.find-sales-representative__dropdown-list > div:nth-child(2) > div > select'}
    all_checkbox = {"by": By.CSS_SELECTOR,
                    "value": 'div.find-sales-representative__checkbox-list > div > div:nth-child(1)'}
    kemet_sales_office_checkbox = {"by": By.CSS_SELECTOR,
                                   "value": 'div.find-sales-representative__checkbox-list > div > div:nth-child(2)'}
    manufacturers_rep_checkbox = {"by": By.CSS_SELECTOR,
                                  "value": 'div.find-sales-representative__checkbox-list > div > div:nth-child(3)'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    def get_current_url(self):
        return self._get_current_url()

    def hover_over_where_to_buy(self):
        self._hover(self.where_to_buy_tab)

    def click_on_find_a_distributor(self):
        self._click(self.find_a_distri)

    def click_on_find_a_sales_rep(self):
        self._click(self.find_a_sales_rep)

    # Find A Distributor page
    def click_on_region_drop_down_menu(self):
        self._click(self.region_option_drop_down_menu_distri)

    def select_option_from_the_region_drop_down(self, region):
        self._select_dropdown_option(self.region_option_drop_down_menu_distri, region)

    def click_on_country_drop_down_menu(self):
        self._click(self.country_option_drop_down_menu_distri)

    def select_option_from_the_country_drop_down(self, country):
        self._select_dropdown_option(self.country_option_drop_down_menu_distri, country)

    def get_global_distributors_items(self):
        elems = self.driver.find_elements_by_css_selector('div.find-kemet-distributor__global-distributors > div > div')
        return elems

    def get_global_distributors_items_count(self):
        return len(self.get_global_distributors_items())

    def get_regional_distributors_items(self):
        elems = self.driver.find_elements_by_css_selector(
            'div.find-kemet-distributor__regional-distributors > div > div')
        return elems

    def get_regional_distributors_items_count(self):
        return len(self.get_regional_distributors_items())

    # ---------------------------------------------------------------

    # Find A Sales Representative
    def click_on_region_drop_down_menu_sales_rep(self):
        self._click(self.region_option_drop_down_menu_sales_rep)

    def select_option_from_the_region_drop_down_sales_rep(self, region):
        self._select_dropdown_option(self.region_option_drop_down_menu_sales_rep, region)

    def click_on_country_drop_down_menu_sales_rep(self):
        self._click(self.state_option_drop_down_menu_sales_rep)

    def select_option_from_the_country_drop_down_sales_rep(self, country):
        self._select_dropdown_option(self.state_option_drop_down_menu_sales_rep, country)

    def get_sales_reps_items(self):
        elems = self.driver.find_elements_by_css_selector(
            'div.find-sales-representative__distributors > div > div > div')
        return elems

    def get_sales_reps_items_count(self):
        return len(self.get_sales_reps_items())

    def select_all_checkbox(self):
        self._click(self.all_checkbox)

    def select_kemet_sales_office_checkbox(self):
        self._click(self.kemet_sales_office_checkbox)

    def select_manufacturers_rep_checkbox(self):
        self._click(self.manufacturers_rep_checkbox)
