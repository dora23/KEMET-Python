from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class Header(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    header_section = {"by": By.CSS_SELECTOR, "value": 'header > div.header__central-nav'}
    header_logo = {"by": By.CLASS_NAME, "value": 'header__nav-logo-link'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    applications_tab = {"by": By.ID, "value": 'subNav_2-link'}
    design_tab = {"by": By.ID, "value": 'subNav_3-link'}
    engineering_center_tab = {"by": By.ID, "value": 'subNav_4-link'}
    support_tab = {"by": By.ID, "value": 'subNav_5-link'}
    about_tab = {"by": By.ID, "value": 'subNav_6-link'}
    search_field = {"by": By.ID, "value": 'header__search-form'}
    partner_hub = {"by": By.CSS_SELECTOR, "value": 'ul.header__quick-utilities.show-for-xlarge > li:nth-child(1) > a'}
    where_to_buy = {"by": By.CSS_SELECTOR, "value": 'ul.header__quick-utilities.show-for-xlarge > li:nth-child(2) > a'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def header_navigation_is_displayed(self):
        return self._is_displayed(self.header_section)

    def header_logo_is_displayed(self):
        return self._is_displayed(self.header_logo)

    def products_tab_is_displayed(self):
        return self._is_displayed(self.products_tab)

    def application_tab_is_displayed(self):
        return self._is_displayed(self.applications_tab)

    def design_tab_is_displayed(self):
        return self._is_displayed(self.design_tab)

    def engineering_center_tab_is_displayed(self):
        return self._is_displayed(self.applications_tab)

    def support_tab_is_displayed(self):
        return self._is_displayed(self.support_tab)

    def about_tab_is_displayed(self):
        return self._is_displayed(self.about_tab)

    def search_field_is_displayed(self):
        return self._is_displayed(self.search_field)

    def partner_hub_is_displayed(self):
        return self._is_displayed(self.partner_hub)

    def where_to_buy_is_displayed(self):
        return self._is_displayed(self.where_to_buy)