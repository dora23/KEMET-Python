import pytest
from pages import footer


class TestFooterSection():
    @pytest.fixture()
    def footer_section(self, driver):
        return footer.Footer(driver)

    def test_footer_elements_present(self, footer_section):
        footer_section.navigate_to_kemet_page()

        if footer_section.footer_navigation_is_displayed():
            assert footer_section.need_help_section_is_displayed()
            assert footer_section.support_section_is_displayed()
            assert footer_section.products_section_is_displayed()
            assert footer_section.about_kemet_section_is_displayed()
            assert footer_section.follow_us_section_is_displayed()
            assert footer_section.subscribe_section_is_displayed()
            pass
            print("All the footer elements are present")
        else:
            print("The footer section is missing")
