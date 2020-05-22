import time

import pytest

from pages.header_section import applications_nav_section
from tests import config


class TestApplicationsMenu:
    @pytest.fixture()
    def apps(self, driver):
        return applications_nav_section.ApplicationsSection(driver)

    # Print all application categories
    def test_applications_nav_menu(self, apps):
        apps.navigate_to_kemet_page()
        time.sleep(2)
        apps.accept_cookies()
        apps.hover_over_applications()
        time.sleep(2)
        print('\nIndustry Applications:')
        displayed_industry_apps_elems_title = apps.get_displayed_industry_apps_elems_titles()
        industry_apps_elems = []
        for title in displayed_industry_apps_elems_title:
            title_among_possible = False
            if title.text in config.possible_industry_applications:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            industry_apps_elems.append(title.text)
            print(title.text)
        print('\nTechnology Applications:')
        displayed_tech_apps_elems_title = apps.get_displayed_technology_apps_elems_titles()
        industry_apps_elems = []
        for title in displayed_tech_apps_elems_title:
            title_among_possible = False
            if title.text in config.possible_technology_applications:
                title_among_possible = True
            assert title_among_possible, "Titles don't match"
            industry_apps_elems.append(title.text)
            print(title.text)