import pytest


@pytest.mark.regression
def test_eco_friendly_add_to_cart(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.select_product()
    eco_friendly_page.find_product_in_cart()
    eco_friendly_page.check_product_in_cart("Ana Running Short")
    eco_friendly_page.delete_product()


@pytest.mark.regression
def test_eco_friendly_page(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_product_count()
    eco_friendly_page.check_visible_and_clickable()
    eco_friendly_page.check_product_size()
    eco_friendly_page.check_product_price()
