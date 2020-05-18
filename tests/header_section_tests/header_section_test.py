import time

import pytest
from pages import header


class TestHeaderSection():
    @pytest.fixture()
    def header(self, driver):
        return header.Header(driver)

    def test_header_elements_present(self, header):
        header.navigate_to_kemet_page()
        time.sleep(5)

        if header.header_navigation_is_displayed():
            assert header.header_logo_is_displayed()
            assert header.products_tab_is_displayed()
            assert header.application_tab_is_displayed()
            assert header.engineering_center_tab_is_displayed()
            assert header.support_tab_is_displayed()
            assert header.about_tab_is_displayed()
            assert header.search_field_is_displayed()
            assert header.partner_hub_is_displayed()
            assert header.where_to_buy_is_displayed()
            pass
            print("All the header elements are present")
        else:
            print("The header section is missing")
