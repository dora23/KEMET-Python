from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class ProductsSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    capacitors_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_1-link'}
    emc_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_2-link'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    # Products Main Nav Section
    def hover_over_the_products_main_nav(self):
        self._hover(self.products_tab)

    def get_products_sub_nav_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#subSubNav_1 > div.header__sub-nav-content > ul > li')
        return elems

    def get_products_sub_nav_items_count(self):
        return len(self.get_products_sub_nav_items())

    # ---------------------------------------------------

    # Capacitors Sub Nav Section
    def hover_over_the_capacitors_sub_nav(self):
        self._hover(self.capacitors_sub_nav_tab)

    def get_capacitors_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#subSubNav_1 > div.header__sub-nav-content > ul > li')
        return elems

    def get_capacitors_items_count(self):
        return len(self.get_capacitors_items())

    # ---------------------------------------------------

    # EMC Sub Nav Section
    def hover_over_the_emc_sub_nav(self):
        self._hover(self.emc_sub_nav_tab)

    def get_emc_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#subSubNav_2 > div.header__sub-nav-content > ul > li')
        return elems

    def get_emc_items_count(self):
        return len(self.get_emc_items())
    # ---------------------------------------------------
