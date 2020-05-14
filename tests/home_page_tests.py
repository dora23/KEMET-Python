import pytest
import time

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
            # Verifies that the correct page is opened when clicked on a promo 4 component
            displayed_promo_tiles_elems_title = home.get_displayed_promo4_tiles_elems_titles()
            promo4_tiles_elems = []
            for title in displayed_promo_tiles_elems_title:
                title_among_possible = False
                if title.text in config.possible_promo4_titles:
                    title_among_possible = True
                assert title_among_possible, "Titles don't match"
                promo4_tiles_elems.append((title.get_attribute("href"), title.text))
                print("\n" + title.text)
            for promo4_tiles_elem in promo4_tiles_elems:
                home._visit2(promo4_tiles_elem[0])
                time.sleep(2)
                assert home.get_current_url() == promo4_tiles_elem[0]
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
            # Verifies that the correct page is opened when clicked on a marketing tile component
            displayed_marketing_tiles_elems_title = home.get_displayed_marketing_tiles_elems_titles()
            marketing_tiles_elems = []
            for title in displayed_marketing_tiles_elems_title:
                title_among_possible = False
                if title.text in config.possible_marketing_titles:
                    title_among_possible = True
                assert title_among_possible, "Titles don't match"
                marketing_tiles_elems.append((title.get_attribute("href"), title.text))
                print("\n" + title.text)
            for marketing_tiles_elem in marketing_tiles_elems:
                home._visit2(marketing_tiles_elem[0])
                time.sleep(2)
                assert home.get_current_url() == marketing_tiles_elem[0]
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
            # Verifies that the correct page is opened when clicked on a promo tile element
            displayed_promo_tiles_elems_title = home.get_displayed_promo_tiles_elems_titles()
            promo_tiles_elems = []
            for title in displayed_promo_tiles_elems_title:
                title_among_possible = False
                if title.text in config.possible_promo_titles:
                    title_among_possible = True
                assert title_among_possible, "Titles don't match"
                promo_tiles_elems.append((title.get_attribute("href"), title.text))
                print('\n' + title.text)
            for promo_tiles_elem in promo_tiles_elems:
                home._visit2(promo_tiles_elem[0])
                time.sleep(2)
                assert home.get_current_url() == promo_tiles_elem[0]
        else:
            print("The Promo Tiles Component is not displayed on the page!")

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
    # -------------------------------------------------------------------------------------------------------`
