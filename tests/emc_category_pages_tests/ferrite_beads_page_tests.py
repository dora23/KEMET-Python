import time

import pytest

from pages.emc_category_pages import ferrite_beads_page


class TestFerriteBeadsPage:
    @pytest.fixture()
    def ferrite_beads(self, driver):
        return ferrite_beads_page.FerriteBeadsPage(driver)

    def test_ferrite_beads_sub_categories(self, ferrite_beads):
        ferrite_beads.navigate_to_kemet_page()
        time.sleep(2)
        ferrite_beads.accept_cookies()
        ferrite_beads.hover_over_the_products_main_nav()
        ferrite_beads.hover_over_the_emc_sub_nav()
        ferrite_beads.click_on_ferrite_beads_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/ferrite-beads.html" == ferrite_beads.get_current_url()), \
            "This is not the Ferrite Beads page!"
        assert ferrite_beads.browse_tab_is_displayed()
        assert ferrite_beads.datasheets_tab_is_displayed()
