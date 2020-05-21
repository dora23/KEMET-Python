from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class TransformersPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    transformers_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_8-link'}

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

    def click_on_the_transformers_sub_nav(self):
        self._click(self.transformers_sub_nav_tab)

