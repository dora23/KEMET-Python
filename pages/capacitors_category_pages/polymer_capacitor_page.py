from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class PolymerCapacitorsPages(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    capacitors_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_1-link'}
    polymer_category = {"by": By.CSS_SELECTOR,
                        "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(2) > a'}
    polymer_page_slick_list = {"by": By.CSS_SELECTOR, "value": '#panel1c > div.category-tiles > div > div > div'}
    all_polymer_sub_category = {"by": By.CSS_SELECTOR,
                                "value": 'div.category-tiles__item.category-tiles__item--text.active.slick-slide.slick-current.slick-active > a'}

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

    def click_on_polymer_category(self):
        self._click(self.polymer_category)

    def polymer_category_slick_list_is_displayed(self):
        return self._is_displayed(self.polymer_page_slick_list)

    def all_polymer_displayed(self):
        return self._is_displayed(self.all_polymer_sub_category)

    def get_polymer_slick_list_items(self):
        elems = self.driver.find_elements_by_css_selector('div.category-tiles__item')
        return elems

    def get_polymer_slick_list_items_count(self):
        return len(self.get_polymer_slick_list_items())
