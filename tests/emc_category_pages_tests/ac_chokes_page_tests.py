import time

import pytest

from pages.emc_category_pages import ac_chokes_page


class TestAcChokesPage:
    @pytest.fixture()
    def ac_chokes(self, driver):
        return ac_chokes_page.AcChokesPage(driver)

    def test_ac_chokes_sub_categories(self, ac_chokes):
        ac_chokes.navigate_to_kemet_page()
        time.sleep(2)
        ac_chokes.accept_cookies()
        ac_chokes.hover_over_the_products_main_nav()
        ac_chokes.hover_over_the_emc_sub_nav()
        ac_chokes.click_on_ac_chokes_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/ac-chokes.html" == ac_chokes.get_current_url()), \
            "This is not the AC Chokes page!"
        assert ac_chokes.browse_tab_is_displayed()
        assert ac_chokes.datasheets_tab_is_displayed()
