import pytest


@pytest.mark.regression
def test_page_ana_running_short(ana_running_short_page):
    ana_running_short_page.open_ana_running_short_page()
    ana_running_short_page.add_product_to_cart()
    ana_running_short_page.check_count('1')
    ana_running_short_page.check_product_in_cart('Ana Running Short')



@pytest.mark.regression
def test_check_add_to_cart_with_out_selected_size_color(ana_running_short_page):
    ana_running_short_page.open_ana_running_short_page()
    ana_running_short_page.check_add_to_cart_with_out_selected_size_color('This is a required field.')

