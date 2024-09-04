from pages.locators import sale_locators as loc
from pages.base_page import BasePage


class SalePage(BasePage):
    page_url = 'sale.html#'
    bags_url = 'gear/bags.html'
    jacket_url = 'women/tops-women/jackets-women.html?product_list_order=price"'
    shorts_url = 'men/bottoms-men/shorts-men.html'

    def click_jacket(self):
        jacket = self.find(loc.jacket_loc)
        jacket.click()

    def check_title(self, text):
        page_title = self.find(loc.page_title_loc)
        assert page_title.text == text

    def click_bags(self):
        bags = self.find(loc.bags_loc)
        bags.click()

    def check_bags_title(self, text):
        title = self.find(loc.title_loc)
        assert title.text == text

    def check_visible_and_clickable(self):
        products = self.find_all(loc.products_loc)
        for index, product in enumerate(products):
            is_clickable = self.driver.execute_script("return arguments[0].offsetParent !== null;", product)
            assert is_clickable, f"Продукт {index + 1} не кликабелен."
            print(f"Продукт {index + 1} кликабелен.")

    def check_product_price(self):
        products1 = self.find_all(loc.products1_loc)
        for index, product in enumerate(products1, start=1):
            price_element = self.find(loc.product_loc)
            assert price_element is not None, f"Цена не найдена для продукта {index}."
            assert price_element.text != "", f"Цена для продукта {index} пуста."
            print(f"Продукт {index} имеет цену: {price_element.text}")

    def check_product_size(self):
        products1 = self.find_all(loc.products1_loc)
        for index, product in enumerate(products1, start=1):
            size_element = self.find(loc.prod_loc)
            assert size_element is not None, f"Размер не найден для продукта {index}."
            assert size_element.text != "", f"Размер для продукта {index} пуст."
            print(f"Продукт {index} имеет размеры: {size_element.text}")

    def check_product_count(self):
        products = self.find_all(loc.products_loc)
        product_count = len(products)
        expected_count = 12
        assert product_count == expected_count
