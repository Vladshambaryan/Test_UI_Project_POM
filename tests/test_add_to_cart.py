import pytest


@pytest.mark.regression
def test_add_to_cart(add_to_cart_page):
    add_to_cart_page.open_add_to_cart_page()
    add_to_cart_page.add_product_to_cart()
    add_to_cart_page.check_count()
    add_to_cart_page.check_product_in_cart()


@pytest.mark.regression
def test_check_add_to_cart_with_out_selected_size_color(add_to_cart_page):
    add_to_cart_page.open_add_to_cart_page()
    add_to_cart_page.check_add_to_cart_with_out_selected_size_color()
