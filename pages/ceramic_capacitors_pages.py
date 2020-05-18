from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class CeramicCapacitorsPages(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    capacitors_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_1-link'}
    browse_by_title = {"by": By.CSS_SELECTOR,
                       "value": '#category-browse-by > div > div > div.browse-by__header.grid-x > div > h3'}

    ceramic_category = {"by": By.CSS_SELECTOR,
                        "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(1) > a'}
    ceramic_page_slick_list = {"by": By.CSS_SELECTOR, "value": '#panel1c > div.category-tiles > div > div > div'}
    slick_list_right_arrow = {"by": By.CSS_SELECTOR, "value": 'span.icon-chevron-right.slick-arrow'}
    all_ceramic_sub_category = {"by": By.CSS_SELECTOR, "value": 'div.category-tiles__item.category-tiles__item--text.active.slick-slide.slick-current.slick-active > a'}

    # polymer_category = {"by": By.ID, "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(2) > a'}
    # tantalum_category = {"by": By.ID, "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(3) > a'}
    # aluminium_category = {"by": By.ID, "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(4) > a'}
    # film_category = {"by": By.ID, "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(5) > a'}
    # supercapacitors_category = {"by": By.ID, "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(6) > a'}

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

    def get_browse_by_title_text(self):
        return self._get_text(self.browse_by_title)

    def click_on_ceramic_category(self):
        self._click(self.ceramic_category)

    def ceramic_category_slick_list_is_displayed(self):
        return self._is_displayed(self.ceramic_page_slick_list)

    def all_ceramic_displayed(self):
        return self._is_displayed(self.all_ceramic_sub_category)

    def click_on_slick_list_right_arrow(self):
        self._click(self.slick_list_right_arrow)

    def get_ceramic_slick_list_items(self):
        elems = self.driver.find_elements_by_css_selector('div.category-tiles__item')
        return elems

    def get_ceramic_slick_list_items_count(self):
        return len(self.get_ceramic_slick_list_items())
