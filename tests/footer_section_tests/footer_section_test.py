import pytest
from selenium.webdriver.common.by import By

from pages.footer_section import footer


class TestFooterSection:
    @pytest.fixture()
    def footer_section(self, driver):
        return footer.Footer(driver)

    def test_footer_elements_present(self, footer_section):
        footer_section.navigate_to_kemet_page()

        if footer_section.footer_navigation_is_displayed():
            assert footer_section.need_help_section_is_displayed()
            assert footer_section.support_section_is_displayed()
            assert footer_section.products_section_is_displayed()
            assert footer_section.about_kemet_section_is_displayed()
            assert footer_section.follow_us_section_is_displayed()
            assert footer_section.subscribe_section_is_displayed()
            print("\n Copyright text: " + footer_section.get_copyright_text())
            print("All the footer elements are present")
        else:
            print("The footer section is missing")

        # Print Support column items titles
        print("\n-----------Support---------------")
        support_items_number = footer_section.get_support_items_count()
        for i in range(1, support_items_number + 1):
            locator = {"by": By.CSS_SELECTOR,
                       "value": "div.footer__wrapper > div:nth-child(1) > div:nth-child(2) > ul > li:nth-child(" + str(
                           i) + ") > a"}
            support_item_title = footer_section.find_items(locator)
            print("\n" + support_item_title.text)

        # Print Product column items titles
        print("\n-----------Products---------------")
        products_items_number = footer_section.get_products_items_count()
        for j in range(1, products_items_number + 1):
            locator2 = {"by": By.CSS_SELECTOR,
                        "value": "div.footer__column.footer__column--seperated-large > div:nth-child(1) > ul > li:nth-child(" + str(
                            j) + ") > a"}
            products_item_title = footer_section.find_items(locator2)
            print("\n" + products_item_title.text)

        # Print About KEMET column items titles
        print("\n-----------About KEMET---------------")
        about_items_number = footer_section.get_about_items_count()
        for k in range(1, about_items_number + 1):
            locator3 = {"by": By.CSS_SELECTOR,
                        "value": "div.footer__column.footer__column--seperated-large > div:nth-child(2) > ul > li:nth-child(" + str(
                            k) + ") > a"}
            about_item_title = footer_section.find_items(locator3)
            print("\n" + about_item_title.text)

        # Print Follow Us column items links
        print("\n-----------Follow Us---------------")
        follow_us__items_number = footer_section.get_follow_us_items_count()
        for l in range(1, follow_us__items_number + 1):
            item_name = {"by": By.CSS_SELECTOR,
                         "value": "div.footer__column.footer__column--form > div:nth-child(1) > ul > li:nth-child(" + str(
                             l) + ") > a > span.show-for-sr"}
            item_link = {"by": By.CSS_SELECTOR,
                         "value": "div.footer__column.footer__column--seperated-large > div:nth-child(2) > ul > li:nth-child(" + str(
                             l) + ") > a"}
            follow_us_name = footer_section.find_items(item_name)
            follow_us_link = footer_section.find_items(item_link)
            print("\n" + follow_us_name.text + ": " + follow_us_link.get_attribute("href"))
