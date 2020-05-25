from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class EngineeringKitsPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    engineering_kits_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_9-link'}
    browse_tab = {"by": By.CSS_SELECTOR, "value": '#in-page-tabs > li:nth-child(1)'}
    browse_by_title = {"by": By.CSS_SELECTOR,
                       "value": '#category-browse-by > div > div > div.browse-by__header.grid-x > div > h3'}
    slick_list_right_arrow = {"by": By.CSS_SELECTOR, "value": 'span.icon-chevron-right.slick-arrow'}
    engineering_kits_devices_page_slick_list = {"by": By.CSS_SELECTOR,
                                             "value": '#panel1c > div.category-tiles > div > div > div'}
    all_engineering_kits_devices_sub_category = {"by": By.CSS_SELECTOR,
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

    def click_on_the_engineering_kits_sub_nav(self):
        self._click(self.engineering_kits_sub_nav_tab)

    def get_browse_by_title_text(self):
        return self._get_text(self.browse_by_title)

    def browse_tab_is_displayed(self):
        return self._is_displayed(self.browse_tab)

    def engineering_kits_category_slick_list_is_displayed(self):
        return self._is_displayed(self.engineering_kits_devices_page_slick_list)

    def all_engineering_kits_displayed(self):
        return self._is_displayed(self.all_engineering_kits_devices_sub_category)

    def slick_list_right_arrow_is_displayed(self):
        return self._is_displayed(self.slick_list_right_arrow)

    def click_on_slick_list_right_arrow(self):
        self._click(self.slick_list_right_arrow)

    def get_displayed_subcategory_tiles_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector(
            'div.category-tiles__item > a > div.category-tiles__item-info > span')
        return _elems
