import time

import pytest

from pages.header_section import support_nav_section
from tests import config


class TestSupportMenu:
    @pytest.fixture()
    def support(self, driver):
        return support_nav_section.SupportSection(driver)

    # Print all Support categories and test their links
    def test_applications_nav_menu(self, support):
        support.navigate_to_kemet_page()
        time.sleep(2)
        support.accept_cookies()
        support.hover_over_support()
        time.sleep(2)
        print('\nSupport:')
        displayed_contact_us_elems_title = support.get_displayed_support_contact_us_titles()
        support_apps_elems = []
        for title in displayed_contact_us_elems_title:
            title_among_possible = False
            if title.text in config.possible_support_column_1:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            support_apps_elems.append((title.get_attribute("href"), title.text))
            print(title.text)
        for support_1_elem in support_apps_elems:
            support._visit2(support_1_elem[0])
            time.sleep(2)
            assert support.get_current_url() == support_1_elem[0]
        support.hover_over_support()
        displayed_supply_management_elems_title = support.get_displayed_technology_supply_management_elems_titles()
        for title in displayed_supply_management_elems_title:
            title_among_possible = False
            if title.text in config.possible_support_column_2:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            support_apps_elems.append((title.get_attribute("href"), title.text))
            print(title.text)
        for support_2_elem in support_apps_elems:
            support._visit2(support_2_elem[0])
            time.sleep(2)
            assert support.get_current_url() == support_2_elem[0]