import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import film_capacitor_page


class TestFilmCapacitorsPage:
    @pytest.fixture()
    def film(self, driver):
        return film_capacitor_page.FilmCapacitorsPage(driver)

    # Test Film Capacitor Slick Nav
    def test_film_sub_categories(self, film):
        film.navigate_to_kemet_page()
        time.sleep(2)
        film.accept_cookies()
        film.hover_over_the_products_main_nav()
        film.hover_over_the_capacitors_sub_nav()
        film.click_on_film_category()
        time.sleep(2)
        assert ("https://www.kemet.com/en/us/capacitors/film.html" == film.get_current_url()), \
            "This is not the Film Capacitor page!"
        if film.film_category_slick_list_is_displayed:
            if film.all_film_displayed():
                film_slick_list_item_number = film.get_film_slick_list_items_count()
                print("\nFilm Capacitors Sub Categories:")
                for i in range(2, film_slick_list_item_number + 1):
                    locator = {"by": By.CSS_SELECTOR,
                               "value": "div.category-tiles__item:nth-child(" + str(
                                   i) + ") > a > div.category-tiles__item-info > span"}
                    sub_category_item_title = film.find_items(locator)
                    print(sub_category_item_title.text)
            else:
                print("The All FIlm Capacitors tab is not displayed")
        else:
            print("The Slick list is not displayed")
