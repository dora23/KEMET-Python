from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class SupportSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    support_tab = {"by": By.ID, "value": 'subNav_5-link'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    def get_current_url(self):
        return self._get_current_url()

    def hover_over_support(self):
        self._hover(self.support_tab)

    def get_displayed_support_contact_us_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            '#subNav_5 > div.header__sub-nav-content > div:nth-child(1) > ul > li > a')
        return _elems

    def get_displayed_technology_supply_management_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            '#subNav_5 > div.header__sub-nav-content > div:nth-child(2) > ul > li> a')
        return _elems