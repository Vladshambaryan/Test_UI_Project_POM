import pytest


@pytest.mark.regression
def test_add_to_cart(add_to_cart_page):
    add_to_cart_page.open_add_to_cart_page()
    add_to_cart_page.add_product_to_cart()
    add_to_cart_page.check_count('1')
    add_to_cart_page.check_product_in_cart('Ana Running Short')


@pytest.mark.regression
def test_check_add_to_cart_with_out_selected_size_color(add_to_cart_page):
    add_to_cart_page.open_add_to_cart_page()
    add_to_cart_page.check_add_to_cart_with_out_selected_size_color('This is a required field.')
