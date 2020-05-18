from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class AluminiumCapacitorsPages(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    capacitors_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_1-link'}
    browse_by_title = {"by": By.CSS_SELECTOR,
                       "value": '#category-browse-by > div > div > div.browse-by__header.grid-x > div > h3'}
    aluminium_category = {"by": By.CSS_SELECTOR,
                        "value": '#subSubNav_1 > div.header__sub-nav-content > ul > li:nth-child(4) > a'}
    aluminium_page_slick_list = {"by": By.CSS_SELECTOR, "value": '#panel1c > div.category-tiles > div > div > div'}
    slick_list_right_arrow = {"by": By.CSS_SELECTOR, "value": 'span.icon-chevron-right.slick-arrow'}
    all_aluminium_sub_category = {"by": By.CSS_SELECTOR, "value": 'div.category-tiles__item.category-tiles__item--text.active.slick-slide.slick-current.slick-active > a'}

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

    def click_on_aluminium_category(self):
        self._click(self.aluminium_category)

    def aluminium_category_slick_list_is_displayed(self):
        return self._is_displayed(self.aluminium_page_slick_list)

    def all_aluminium_displayed(self):
        return self._is_displayed(self.all_aluminium_sub_category)

    def click_on_slick_list_right_arrow(self):
        self._click(self.slick_list_right_arrow)

    def get_aluminium_slick_list_items(self):
        elems = self.driver.find_elements_by_css_selector('div.category-tiles__item')
        return elems

    def get_aluminium_slick_list_items_count(self):
        return len(self.get_aluminium_slick_list_items())