from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import sale_locators as loc
from pages.locators import eco_friendly_locator as ecoloc
from pages.base_page import BasePage


class EcoFriendly(BasePage):
    page_url = 'collections/eco-friendly.html'

    def open_page_eco_friendly(self):
        self.driver.get(f'{self.base_url}/{self.page_url}')

    def select_product(self):
        short = self.find(ecoloc.short_loc)
        short.click()
        size = self.find(ecoloc.size_loc)
        size.click()
        color = self.find(ecoloc.color_loc)
        color.click()
        add_to_cart = self.find(ecoloc.add_to_cart_loc)
        add_to_cart.click()

    def find_product_in_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[@class='counter-number']"), '1'))
        self.find(ecoloc.counter_loc)
        count = self.find(ecoloc.counter_loc)
        count.click()
        view = self.find(ecoloc.view_loc)
        view.click()

    def check_product_in_cart(self, text):
        short1 = self.find(ecoloc.short1_loc)
        assert short1.text == text

    def delete_product(self):
        delete = self.find(ecoloc.delete_loc)
        delete.click()

    def check_product_count(self):
        products = self.find_all(loc.products_loc)
        product_count = len(products)
        expected_count = product_count
        assert product_count == expected_count

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
