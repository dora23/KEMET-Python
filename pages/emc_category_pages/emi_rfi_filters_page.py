from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class EmiRfiFiltersPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    products_tab = {"by": By.ID, "value": 'subNav_1-link'}
    emc_sub_nav_tab = {"by": By.ID, "value": 'subSubNav_2-link'}
    emi_rfi_filters_category = {"by": By.CSS_SELECTOR,
                          "value": '#subSubNav_2 > div.header__sub-nav-content > ul > li:nth-child(6) > a'}
    browse_tab = {"by": By.CSS_SELECTOR, "value": '#in-page-tabs > li:nth-child(1)'}
    datasheets_tab = {"by": By.CSS_SELECTOR, "value": '#in-page-tabs > li:nth-child(2)'}
    browse_by_title = {"by": By.CSS_SELECTOR,
                       "value": '#category-browse-by > div > div > div.browse-by__header.grid-x > div > h3'}
    emi_rfi_filters_page_slick_list = {"by": By.CSS_SELECTOR, "value": '#panel1c > div.category-tiles > div > div > div'}
    all_emi_rfi_filters_sub_category = {"by": By.CSS_SELECTOR,
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

    def hover_over_the_emc_sub_nav(self):
        self._hover(self.emc_sub_nav_tab)

    def get_browse_by_title_text(self):
        return self._get_text(self.browse_by_title)

    def click_on_emi_rfi_filters_category(self):
        self._click(self.emi_rfi_filters_category)

    def browse_tab_is_displayed(self):
        return self._is_displayed(self.browse_tab)

    def datasheets_tab_is_displayed(self):
        return self._is_displayed(self.datasheets_tab)

    def emi_rfi_filters_category_slick_list_is_displayed(self):
        return self._is_displayed(self.emi_rfi_filters_page_slick_list)

    def all_emi_rfi_filters_displayed(self):
        return self._is_displayed(self.all_emi_rfi_filters_sub_category)

    def get_emi_rfi_filters_slick_list_items(self):
        elems = self.driver.find_elements_by_css_selector('div.category-tiles__item')
        return elems

    def get_emi_rfi_filters_slick_list_items_count(self):
        return len(self.get_emi_rfi_filters_slick_list_items())
