from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class Footer(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    footer_section = {"by": By.CLASS_NAME, "value": 'footer'}
    need_help = {"by": By.CSS_SELECTOR, "value": 'div.footer__wrapper > div:nth-child(1) > div:nth-child(1)'}
    support = {"by": By.CSS_SELECTOR, "value": 'div.footer__wrapper > div:nth-child(1) > div:nth-child(2)'}
    products = {"by": By.CSS_SELECTOR, "value": 'div.footer__column.footer__column--seperated-large > div:nth-child(1)'}
    about_kemet = {"by": By.CSS_SELECTOR,
                   "value": 'div.footer__column.footer__column--seperated-large > div:nth-child(2)'}
    follow_us = {"by": By.CSS_SELECTOR, "value": 'div.footer__column.footer__column--form > div:nth-child(1)'}
    subscribe = {"by": By.CSS_SELECTOR, "value": 'div.footer__column.footer__column--form > div:nth-child(2)'}
    copyright_text = {"by": By.CLASS_NAME, "value": 'footer__copyright'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def footer_navigation_is_displayed(self):
        return self._is_displayed(self.footer_section)

    def need_help_section_is_displayed(self):
        return self._is_displayed(self.need_help)

    def support_section_is_displayed(self):
        return self._is_displayed(self.support)

    def products_section_is_displayed(self):
        return self._is_displayed(self.products)

    def about_kemet_section_is_displayed(self):
        return self._is_displayed(self.about_kemet)

    def follow_us_section_is_displayed(self):
        return self._is_displayed(self.follow_us)

    def subscribe_section_is_displayed(self):
        return self._is_displayed(self.subscribe)

    def get_copyright_text(self):
        return self._get_text(self.copyright_text)

    def find_items(self, item):
        return self._find(item)

    # Support section
    def get_support_items(self):
        elems = self.driver.find_elements_by_css_selector(
            'div.footer__wrapper > div:nth-child(1) > div:nth-child(2) > ul > li')
        return elems

    def get_support_items_count(self):
        return len(self.get_support_items())

    # Products section
    def get_products_items(self):
        elems = self.driver.find_elements_by_css_selector(
            'div.footer__column.footer__column--seperated-large > div:nth-child(1) > ul > li')
        return elems

    def get_products_items_count(self):
        return len(self.get_products_items())

    # About Kemet section
    def get_about_items(self):
        elems = self.driver.find_elements_by_css_selector(
            'div.footer__column.footer__column--seperated-large > div:nth-child(2) > ul > li')
        return elems

    def get_about_items_count(self):
        return len(self.get_about_items())

    # Follow Us section
    def get_follow_us_items(self):
        elems = self.driver.find_elements_by_css_selector(
            'div.footer__column.footer__column--form > div:nth-child(1) > ul > li')
        return elems

    def get_follow_us_items_count(self):
        return len(self.get_follow_us_items())
