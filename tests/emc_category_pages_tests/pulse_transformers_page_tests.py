import time

import pytest

from pages.emc_category_pages import pulse_transformers_page


class TestPulseTransformersPage:
    @pytest.fixture()
    def pulse_transformers(self, driver):
        return pulse_transformers_page.PulseTransformersPage(driver)

    def test_pulse_transformers_sub_categories(self, pulse_transformers):
        pulse_transformers.navigate_to_kemet_page()
        time.sleep(2)
        pulse_transformers.accept_cookies()
        pulse_transformers.hover_over_the_products_main_nav()
        pulse_transformers.hover_over_the_emc_sub_nav()
        pulse_transformers.click_on_pulse_transformers_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/pulse-transformers.html" == pulse_transformers.get_current_url()), \
            "This is not the Pulse Transformers page!"
        assert pulse_transformers.browse_tab_is_displayed()
        assert pulse_transformers.datasheets_tab_is_displayed()
