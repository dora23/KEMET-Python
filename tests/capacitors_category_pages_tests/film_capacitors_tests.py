import time

import pytest
from selenium.webdriver.common.by import By

from pages.capacitors_category_pages import film_capacitor_page
from tests import config


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
                print("\nFilm Capacitors Sub Categories:")
                displayed_category_tiles_elems_title = film.get_displayed_subcategory_tiles_elems_titles()
                category_tiles_elems = []
                for title in displayed_category_tiles_elems_title:
                    title_among_possible = False
                    if title.text in config.possible_film_capacitor_sub_categories:
                        title_among_possible = True
                    assert title_among_possible, "Titles don't match"
                    category_tiles_elems.append(title.text)
                    print(title.text)
            else:
                print("The All FIlm Capacitors tab is not displayed")
        else:
            print("The Slick list is not displayed")
