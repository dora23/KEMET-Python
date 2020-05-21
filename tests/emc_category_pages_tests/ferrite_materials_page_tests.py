import time

import pytest

from pages.emc_category_pages import ferrite_materials_page


class TestFerriteMaterialsPage:
    @pytest.fixture()
    def ferrite_materials(self, driver):
        return ferrite_materials_page.FerriteMaterialsPage(driver)

    def test_ferrite_materials_sub_categories(self, ferrite_materials):
        ferrite_materials.navigate_to_kemet_page()
        time.sleep(2)
        ferrite_materials.accept_cookies()
        ferrite_materials.hover_over_the_products_main_nav()
        ferrite_materials.hover_over_the_emc_sub_nav()
        ferrite_materials.click_on_ferrite_materials_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/emc/ferrite-materials.html" == ferrite_materials.get_current_url()), \
            "This is not the Ferrite Materials page!"
        assert ferrite_materials.browse_tab_is_displayed()
        assert ferrite_materials.datasheets_tab_is_displayed()
