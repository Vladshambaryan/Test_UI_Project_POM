import pytest


@pytest.mark.regression
def test_sale_page(sale_page):
    sale_page.open_page_sale()
    sale_page.click_jacket()
    sale_page.check_title('Jackets')


@pytest.mark.regression
def test_sale_bags(sale_page):
    sale_page.open_page_sale()
    sale_page.click_bags()
    sale_page.check_bags_title('Bags')


@pytest.mark.regression
def test_visible_and_clickable_bags(sale_page):
    sale_page.open_page_bag()
    sale_page.check_product_count()
    sale_page.check_visible_and_clickable()
    sale_page.check_product_price()


@pytest.mark.regression
def test_visible_and_clickable_jacket(sale_page):
    sale_page.open_page_jacket()
    sale_page.check_product_count()
    sale_page.check_visible_and_clickable()
    sale_page.check_product_price()
    sale_page.check_product_size()


@pytest.mark.regression
def test_visible_and_clickable_shorts(sale_page):
    sale_page.open_page_shorts()
    sale_page.check_product_count()
    sale_page.check_visible_and_clickable()
    sale_page.check_product_price()
    sale_page.check_product_size()
