import time

import pytest

from pages.header_section import about_nav_section
from tests import config


class TestAboutMenu:
    @pytest.fixture()
    def about(self, driver):
        return about_nav_section.AboutSection(driver)

    # Print all About categories and test their links
    def test_about_nav_menu(self, about):
        about.navigate_to_kemet_page()
        time.sleep(2)
        about.accept_cookies()
        about.hover_over_about()
        time.sleep(2)
        print('\nAbout:')
        displayed_about_column1_elems_title = about.get_about_column1_titles()
        about_apps_elems_1 = []
        for title in displayed_about_column1_elems_title:
            title_among_possible = False
            if title.text in config.possible_about_column_1:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            about_apps_elems_1.append((title.get_attribute("href"), title.text))
            print(title.text)
        for about_1_elem in about_apps_elems_1:
            about._visit2(about_1_elem[0])
            time.sleep(2)
            assert about.get_current_url() == about_1_elem[0]

        about.navigate_to_kemet_page()
        about.hover_over_about()

        about_apps_elems_2 = []
        displayed_about_column2_elems_title = about.get_about_column2_titles()
        for title2 in displayed_about_column2_elems_title:
            title_among_possible = False
            if title2.text in config.possible_about_column_2:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            about_apps_elems_2.append((title2.get_attribute("href"), title2.text))
            print(title2.text)
        for about_2_elem in about_apps_elems_2:
            about._visit2(about_2_elem[0])
            time.sleep(2)
            if about_2_elem[0] == about.get_current_url():
                print()
            else:
                print(about_2_elem[0], about.get_current_url())
