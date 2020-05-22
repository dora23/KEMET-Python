from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class ApplicationsSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    applications_tab = {"by": By.ID, "value": 'subNav_2-link'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    def hover_over_applications(self):
        self._hover(self.applications_tab)

    def get_displayed_industry_apps_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            '#subNav_2 > div.header__sub-nav-content > div:nth-child(1) > ul > li > a')
        return _elems

    def get_displayed_technology_apps_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            '#subNav_2 > div.header__sub-nav-content > div:nth-child(2) > ul > li> a')
        return _elems