import time

import pytest

from pages.transformers_category_page import transformers_page


class TestRelaysPage:
    @pytest.fixture()
    def transformers(self, driver):
        return transformers_page.TransformersPage(driver)

    def test_relays_sub_categories(self, transformers):
        transformers.navigate_to_kemet_page()
        time.sleep(2)
        transformers.accept_cookies()
        transformers.hover_over_the_products_main_nav()
        transformers.click_on_the_transformers_sub_nav()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/transformers.html" == transformers.get_current_url()), \
            "This is not the Transformers page!"
    # --------------------------------------------------------------------------------------------------
