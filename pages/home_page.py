from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class HomePage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    cookie_banner_agree = {"by": By.CSS_SELECTOR,
                           "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-confirmation-button'}
    cookie_banner_decline = {"by": By.CSS_SELECTOR,
                             "value": '#hs-en-cookie-confirmation-buttons-area > #hs-eu-decline-button'}
    privacy_policy_agree = {"by": By.CSS_SELECTOR,
                            "value": 'div.advance-wrapper.callout-special-font > a'}

    # Hero Banner section
    hero_banner = {"by": By.CLASS_NAME, "value": 'banner-hero'}
    hero_banner_image = {"by": By.CSS_SELECTOR, "value": 'div.banner-hero__image > picture > img'}
    hero_banner_title = {"by": By.CLASS_NAME, "value": 'banner-hero__title'}
    hero_banner_description = {"by": By.CLASS_NAME, "value": 'banner-hero__description'}
    hero_banner_CTA_button = {"by": By.CSS_SELECTOR,
                              "value": 'div.banner-hero__content > div > div > a'}
    # -----------------------------------------------------------------------------------------

    # Promo 4 Tiles Component
    promo_4_tiles = {"by": By.CLASS_NAME, "value": 'promotiles4x'}
    # -----------------------------------------------------------------------------------------

    marketing_tiles = {"by": By.CLASS_NAME, "value": 'marketingtiles'}

    promo_tiles = {"by": By.CLASS_NAME, "value": 'promo-tiles'}

    # Full Width Banner
    full_width_banner = {"by": By.CLASS_NAME, "value": 'fullwidthbanner'}
    full_width_banner_title = {"by": By.CSS_SELECTOR,
                               "value": 'div.fullwidthbanner > div > div.full-width-banner__text > span'}
    full_width_banner_subtitle = {"by": By.CSS_SELECTOR, "value": 'div.full-width-banner__text > p'}
    full_width_banner_cta_button = {"by": By.CSS_SELECTOR, "value": 'div.full-width-banner__text > a'}
    full_width_banner_image = {"by": By.CSS_SELECTOR, "value": 'div.full-width-banner__image > picture > img'}
    # -----------------------------------------------------------------------------------------

    two_column_promo = {"by": By.CLASS_NAME, "value": 'titledtwocolumnpromo'}

    def navigate_to_kemet_page(self):
        self._visit(baseurl)

    def accept_cookies(self):
        return self._click(self.cookie_banner_agree)

    def click_on_privacy_policy_accept_button(self):
        return self._click(self.privacy_policy_agree)

    # Hero Banner section
    def hero_banner_is_displayed(self):
        return self._is_displayed(self.hero_banner)

    def hero_image_displayed(self):
        return self._is_displayed(self.hero_banner_image)

    def get_hero_image_srcset_attribute(self):
        return self._get_attribute(self.hero_banner_image, "srcset")

    def hero_banner_title_displayed(self):
        return self._is_displayed(self.hero_banner_title)

    def hero_banner_title_text(self):
        return self._get_text(self.hero_banner_title)

    def hero_banner_description_displayed(self):
        return self._is_displayed(self.hero_banner_description)

    def hero_banner_description_text(self):
        return self._get_text(self.hero_banner_description)

    def hero_banner_cta_button_displayed(self):
        return self._is_displayed(self.hero_banner_CTA_button)

    def click_on_hero_banner_cta_button(self):
        return self._click(self.hero_banner_CTA_button)

    def get_current_url(self):
        return self._get_current_url()

    # -----------------------------------------------------------------------------------------

    # Promo 4 Tiles section
    def scroll_to_promo_4_tiles_component(self):
        return self._scroll_to_element(self.promo_4_tiles)

    def promo_4_tiles_is_displayed(self):
        return self._is_displayed(self.promo_4_tiles)

    def get_promo4_tiles_items(self):
        elems = self.driver.find_elements_by_css_selector('div.promotiles4x > div > div > div > a')
        return elems

    def get_promo4_tiles_items_count(self):
        return len(self.get_promo4_tiles_items())

    def find_items(self, item):
        return self._find(item)

    def get_displayed_promo4_tiles_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector('div.promotiles4x > div > div > div > a')
        return _elems

    # -----------------------------------------------------------------------------------------

    # Marketing Tiles section
    def scroll_to_marketing_tiles_component(self):
        return self._scroll_to_element(self.marketing_tiles)

    def marketing_tiles_is_displayed(self):
        return self._is_displayed(self.marketing_tiles)

    def get_marketing_tiles_items(self):
        elems = self.driver.find_elements_by_css_selector('div.marketingtiles > div > div > ul > li')
        return elems

    def get_marketing_tiles_items_count(self):
        return len(self.get_marketing_tiles_items())

    def get_displayed_marketing_tiles_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector('div.marketingtiles > div > div > ul > li > a')
        return _elems

    # -----------------------------------------------------------------------------------------

    # Promo Tiles component
    def scroll_to_promo_tiles_component(self):
        return self._scroll_to_element(self.promo_tiles)

    def promo_tiles_is_displayed(self):
        return self._is_displayed(self.promo_tiles)

    def get_promo_tiles_items(self):
        elems = self.driver.find_elements_by_css_selector('div.promo-tiles > div > div.promo-tiles__cards > a')
        return elems

    def get_promo_tiles_items_count(self):
        return len(self.get_promo_tiles_items())

    def get_displayed_promo_tiles_elems_titles(self):
        _elems = self.driver.find_elements_by_css_selector('div.promo-tiles__cards > a')
        return _elems
    # -----------------------------------------------------------------------------------------

    # Full Width Banner component
    def scroll_to_full_width_banner_component(self):
        return self._scroll_to_element(self.full_width_banner)

    def full_width_banner_is_displayed(self):
        return self._is_displayed(self.full_width_banner)

    def get_banner_title(self):
        return self._get_text(self.full_width_banner_title)

    def get_banner_subtitle(self):
        return self._get_text(self.full_width_banner_subtitle)

    def banner_cta_button_displayed(self):
        return self._is_displayed(self.hero_banner_CTA_button)

    def click_on_banner_cta_button(self):
        return self._click(self.hero_banner_CTA_button)

    def get_full_width_banner_srcset_attribute(self):
        return self._get_attribute(self.full_width_banner_image, "srcset")

    # -----------------------------------------------------------------------------------------

    # Promo Two Column Component
    def scroll_to_two_column_promo_component(self):
        self._scroll_to_element(self.two_column_promo)

    def two_column_promo_is_displayed(self):
        return self._is_displayed(self.two_column_promo)
