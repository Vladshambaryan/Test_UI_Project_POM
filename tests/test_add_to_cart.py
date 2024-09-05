import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_add_to_cart_with_out_selected_size_color(add_to_cart):
    add_to_cart.open_page()
    add_to_cart.add_to_cart_button()
    add_to_cart.check_error('This is a required field.')


@pytest.mark.regression
def test_add_to_cart(add_to_cart):
    add_to_cart.open_page()
    add_to_cart.add_product_in_cart()
    add_to_cart.find_product_in_cart()
    add_to_cart.check_product_in_cart('Ana Running Short')
