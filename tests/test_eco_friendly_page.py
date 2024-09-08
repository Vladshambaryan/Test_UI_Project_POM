import pytest


@pytest.mark.regression
def test_sort_by_price(eco_friendly_page):
    eco_friendly_page.open_friendly_page()
    eco_friendly_page.sort_by_price()


@pytest.mark.regression
def test_eco_friendly_filter_products(eco_friendly_page):
    eco_friendly_page.open_friendly_page()
    eco_friendly_page.filter_products_by_price()
    eco_friendly_page.check_filter_products_by_price('8 Items')


@pytest.mark.regression
def test_search_functionality(eco_friendly_page):
    eco_friendly_page.open_friendly_page()
    eco_friendly_page.search_functionality()
    eco_friendly_page.check_search_functionality('3 Items')


@pytest.mark.regression
def test_visible_and_clickable_web_elements(eco_friendly_page):
    eco_friendly_page.open_friendly_page()
    eco_friendly_page.check_product_count(12)
    eco_friendly_page.check_visible_and_clickable()
    eco_friendly_page.verification_product_names(['Ana Running Short', 'Fiona Fitness Short', 'Daria Bikram Pant',
                                                  'Bella Tank', 'Electra Bra Top', 'Tiffany Fitness Tee',
                                                  'Elisa EverCool™ Tee', 'Layla Tee', 'Ariel Roll Sleeve Sweatshirt',
                                                  'Mithra Warmup Pant', 'Atlas Fitness Tank', 'Argus All-Weather Tank'])
    eco_friendly_page.verification_product_prices(['40.00', '29.00', '40.80', '29.00', '39.00', '28.00',
                                                   '29.00', '29.00', '39.00', '22.40', '18.00', '22.00'])
    eco_friendly_page.verification_product_size(['28', '29', '28', '29', '30', '31', '32', '28', '29', 'XS', 'S', 'M',
                                                 'L', 'XL', 'XS', 'S', 'M', 'L', 'XL', 'XS', 'S', 'M', 'L', 'XL', 'XS',
                                                 'S', 'M', 'L', 'XL', 'XS', 'S', 'M', 'L', 'XL', 'XS', 'S', 'M', 'L',
                                                 'XL', '32', '33', '34', '36', 'XS', 'S', 'M', 'L', 'XL', 'XS', 'S',
                                                 'M', 'L', 'XL'])

