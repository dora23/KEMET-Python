from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class AboutSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    about_tab = {"by": By.ID, "value": 'subNav_6-link'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    def get_current_url(self):
        return self._get_current_url()

    def hover_over_about(self):
        self._hover(self.about_tab)

    def get_about_column1_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            '#subNav_6 > div.header__sub-nav-content > div:nth-child(1) > ul > li > a')
        return _elems

    def get_about_column2_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            '#subNav_6 > div.header__sub-nav-content > div:nth-child(2) > ul > li> a')
        return _elems
