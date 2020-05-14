import pytest
import time

from selenium.webdriver.common.by import By

from pages import home_page
from tests import config


class TestHomePage():
    @pytest.fixture()
    def home(self, driver):
        return home_page.HomePage(driver)

    def test_home_page_component_present(self, home):
        home.navigate_to_kemet_page()
        time.sleep(2)
        home.accept_cookies()
        # home.click_on_privacy_policy_accept_button()

        # Hero Banner section tests
        if home.hero_banner_is_displayed():
            assert home.hero_image_displayed()
            if "/content/dam/kemet/lightning/images/hero-images/x_world_city_space_V1.jpg" == home.get_hero_image_srcset_attribute():
                print("\n The Hero Image is correct")
            else:
                print("\n The Hero Image has been changed")

            if home.hero_banner_title_displayed():
                print(home.hero_banner_title_text())
            else:
                print("\n Check the Hero Banner section. Something is wrong!")

            if home.hero_banner_description_displayed():
                print(home.hero_banner_description_text())
            else:
                print("\n Check the Hero Banner section. Something is wrong!")

            if home.hero_banner_cta_button_displayed():
                time.sleep(5)
                home.click_on_hero_banner_cta_button()
                time.sleep(5)
                if "https://www.kemet.com/en/us/applications.html" == home.get_current_url():
                    print("\n You have reached the Applications page.")
                else:
                    print("\n This is not the Applications page!")
        else:
            print("\n The Hero Banner component is missing from the Home page!")
        # -------------------------------------------------------------------------------------------------------

    # Promo 4 Column component tests
    def test_promo_4_component_present(self, home):
        home.navigate_to_kemet_page()
        time.sleep(2)
        home.accept_cookies()
        home.scroll_to_promo_4_tiles_component()
        time.sleep(2)
        if home.promo_4_tiles_is_displayed():
            number_of_promo_4_tiles = home.get_promo4_tiles_items_count()
            for i in range(1, number_of_promo_4_tiles + 1):
                print("--------------------------------------")
                locator = {"by": By.CSS_SELECTOR,
                           "value": "div.promotiles4x > div > div > div > a:nth-child(" + str(i) + ") > p"}
                promo4_items_title = home.find_items(locator)
                print("\n" + promo4_items_title.text)
        else:
            print("The Promo 4 Tiles Component is not displayed on the page!")
        # -------------------------------------------------------------------------------------------------------

    # Marketing Tiles component tests
    def test_marketing_tiles_component_present(self, home):
        home.navigate_to_kemet_page()
        time.sleep(2)
        home.accept_cookies()
        home.scroll_to_marketing_tiles_component()
        time.sleep(2)
        if home.marketing_tiles_is_displayed():
            number_of_marketing_tiles = home.get_marketing_tiles_items_count()
            for j in range(1, number_of_marketing_tiles + 1):
                print("--------------------------------------")
                locator1 = {"by": By.CSS_SELECTOR,
                            "value": "div.marketingtiles > div > div > ul > li:nth-child(" + str(
                                j) + ") > a > div.marketing-tiles__tile-title"}
                marketing_tiles_items_title = home.find_items(locator1)
                print("\n" + marketing_tiles_items_title.text)
        else:
            print("The Marketing Tiles Component is not displayed on the page!")
        # -------------------------------------------------------------------------------------------------------

    # Promo Tiles Component tests
    def test_promo_tiles_component_present(self, home):
        home.navigate_to_kemet_page()
        time.sleep(2)
        home.accept_cookies()
        home.scroll_to_promo_tiles_component()
        time.sleep(2)
        if home.promo_tiles_is_displayed():
            number_of_promo_tiles = home.get_promo_tiles_items_count()
            for k in range(1, number_of_promo_tiles + 1):
                print("--------------------------------------")
                locator2 = {"by": By.CSS_SELECTOR,
                            "value": "div.promo-tiles__cards > a:nth-child(" + str(
                                k) + ") > div.promo-tiles__card-caption > span"}
                promo_tiles_items_title = home.find_items(locator2)
                print("\n" + promo_tiles_items_title.text)
        else:
            print("The Promo Tiles Component is not displayed on the page!")

        # Verifies that the correct page is opened when clicked on a promo tiles element
        displayed_promo_tiles_elems_title = home.get_displayed_promo_tiles_elems_titles()
        promo_tiles_elems = []
        for title in displayed_promo_tiles_elems_title:
            title_among_possible = False
            if title.text in config.possible_promo_titles:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            promo_tiles_elems.append((title.get_attribute("href"), title.text))
        for promo_tiles_elem in promo_tiles_elems:
            home._visit2(promo_tiles_elem[0])
            time.sleep(2)
            assert home.get_current_url() == promo_tiles_elem[0]


# -------------------------------------------------------------------------------------------------------

# Full Width Banner tests
def test_full_width_banner_component_present(self, home):
    home.navigate_to_kemet_page()
    time.sleep(2)
    home.accept_cookies()
    home.scroll_to_full_width_banner_component()
    if home.full_width_banner_is_displayed():
        assert (
                "/content/dam/kemet/lightning/obsolete/homepage/Full%20Width%20Promo.png" == home.get_full_width_banner_srcset_attribute())
        assert ("Sustainability at KEMET" == home.get_banner_title())
        assert (config.full_width_banner_description == home.get_banner_subtitle())
        if home.banner_cta_button_displayed():
            home.click_on_banner_cta_button()
            time.sleep(2)
            assert (
                    "https://kemet-stage.adobemsbasic.com/en/us/about/sustainability.html" == home.get_current_url())
        else:
            print("The CTA button is not displayed on the Full Width Banner component!")
    else:
        print("The Full Width Banner component is not displayed on the page.")
    # -------------------------------------------------------------------------------------------------------

    # Promo Two Column Component tests
    # home.navigate_to_kemet_page()
    # home.scroll_to_two_column_promo_component()
    # if home.two_column_promo_is_displayed():

# assert home.two_column_promo_is_displayed()
