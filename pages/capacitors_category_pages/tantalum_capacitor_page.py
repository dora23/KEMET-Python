from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class TantalumCapacitorsPages(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    capacitors_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_1-link'}
    tantalum_category = {"by": By.CSS_SELECTOR,
                        "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(3) > a'}
    tantalum_page_slick_list = {"by": By.CSS_SELECTOR, "value": '#panel1c > div.category-tiles > div > div > div'}
    all_tantalum_sub_category = {"by": By.CSS_SELECTOR,
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

    def click_on_tantalum_category(self):
        self._click(self.tantalum_category)

    def tantalum_category_slick_list_is_displayed(self):
        return self._is_displayed(self.tantalum_page_slick_list)

    def all_tantalum_displayed(self):
        return self._is_displayed(self.all_tantalum_sub_category)

    def get_tantalum_slick_list_items(self):
        elems = self.driver.find_elements_by_css_selector('div.category-tiles__item')
        return elems

    def get_tantalum_slick_list_items_count(self):
        return len(self.get_tantalum_slick_list_items())