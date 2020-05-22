from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class EngineeringCenterSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    engineering_center_tab = {"by": By.ID, "value": 'subNav_4-link'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def find_items(self, item):
        return self._find(item)

    def hover_over_engineering_center(self):
        self._hover(self.engineering_center_tab)

    def get_engineering_center_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#subNav_4 > div.header__sub-nav-content > div > ul > li')
        return elems

    def get_engineering_center_items_count(self):
        return len(self.get_engineering_center_items())
