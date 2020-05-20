import time

import pytest

from pages.emc_category_pages import flex_suppressor_page


class TestFlexSuppressorPage:
    @pytest.fixture()
    def flex_suppressor(self, driver):
        return flex_suppressor_page.FlexSuppressorPage(driver)

    def test_flex_suppressor_categories(self, flex_suppressor):
        flex_suppressor.navigate_to_kemet_page()
        time.sleep(2)
        flex_suppressor.accept_cookies()
        flex_suppressor.hover_over_the_products_main_nav()
        flex_suppressor.hover_over_the_emc_sub_nav()
        flex_suppressor.click_on_flex_suppressor_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/flex-suppressor.html" == flex_suppressor.get_current_url()), \
            "This is not the Flex Supressor page!"
        assert flex_suppressor.browse_tab_is_displayed()
        assert flex_suppressor.datasheets_tab_is_displayed()
