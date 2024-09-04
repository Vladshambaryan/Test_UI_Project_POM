# from anyio import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import pytest
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
#
# @pytest.fixture()
# def driver():
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     chrome_driver = webdriver.Chrome(options=options)
#     chrome_driver.implicitly_wait(5)
#     return chrome_driver
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def test_add_product_to_cart(driver):
#     driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
#     short = driver.find_element(By.XPATH, "//img[@alt='Ana Running Short']")
#     short.click()
#     size = driver.find_element(By.ID, 'option-label-size-143-item-171')
#     size.click()
#     color = driver.find_element(By.ID, "option-label-color-93-item-56")
#     color.click()
#     add_cart = driver.find_element(By.XPATH, "//span[contains(.,'Add to Cart')]")
#     add_cart.click()
#     WebDriverWait(driver, 15).until(
#         EC.text_to_be_present_in_element((By.XPATH, "//span[@class='counter-number']"), '1'))
#     count = driver.find_element(By.XPATH, "//span[@class='counter-number']")
#     assert count.text == '1'
#     count.click()
#     item_in_cart = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Ana Running Short')]")))
#     assert item_in_cart.text == 'Ana Running Short'
#
#
# #  =========================================================================================
#
# def test_check_add_to_cart(driver):
#     driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
#     short = driver.find_element(By.XPATH, "//img[@alt='Ana Running Short']")
#     short.click()
#     size = driver.find_element(By.ID, 'option-label-size-143-item-171')
#     size.click()
#     color = driver.find_element(By.ID, "option-label-color-93-item-56")
#     color.click()
#     add_cart = driver.find_element(By.XPATH, "//span[contains(.,'Add to Cart')]")
#     add_cart.click()
#     WebDriverWait(driver, 7).until(
#         EC.text_to_be_present_in_element((By.XPATH, "//span[@class='counter-number']"), '1'))
#     count = driver.find_element(By.XPATH, "//span[@class='counter-number']")
#     count.click()
#     item_in_cart = driver.find_element(By.XPATH, "//a[contains(.,'Ana Running Short')]")
#     assert item_in_cart.text == 'Ana Running Short'
#
# #  =====================================================
#
# def test_add_to_cart_with_out_selected_size_color(driver):
#     driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
#     short = driver.find_element(By.XPATH, "//img[@alt='Ana Running Short']")
#     short.click()
#     add_cart = driver.find_element(By.XPATH, "//span[contains(.,'Add to Cart')]")
#     add_cart.click()
#
#     select_color = driver.find_element(By.XPATH, "//div[@id='super_attribute[143]-error']")
#     assert select_color.text == 'This is a required field.'
#     select_size = driver.find_element(By.XPATH, "//div[@id='super_attribute[93]-error']")
#     assert select_size.text == 'This is a required field.'
#
#
#
# #  ==================================================================
#
#
# def test_create_account_with_incorrect_fname(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
#     first = driver.find_element(By.ID, 'firstname')
#     last = driver.find_element(By.ID, 'lastname')
#     email = driver.find_element(By.ID, 'email_address')
#     password = driver.find_element(By.ID, 'password')
#     conf_password = driver.find_element(By.ID, 'password-confirmation')
#     button = driver.find_element(By.CSS_SELECTOR, '.submit')
#     first.send_keys('``V')
#     last.send_keys('Mask')
#     email.send_keys('123abc1234@gmail.com')
#     password.send_keys('12345678mM+$VV')
#     conf_password.send_keys('12345678mM+$VV')
#     button.click()
#     error = driver.find_element(By.XPATH, "(//div[contains(.,'First Name is not valid!')])[6]")
#     assert error.text == 'First Name is not valid!'
#
#
# def test_create_account_with_incorrect_lname(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
#     first = driver.find_element(By.ID, 'firstname')
#     last = driver.find_element(By.ID, 'lastname')
#     email = driver.find_element(By.ID, 'email_address')
#     password = driver.find_element(By.ID, 'password')
#     conf_password = driver.find_element(By.ID, 'password-confirmation')
#     button = driver.find_element(By.CSS_SELECTOR, '.submit')
#     first.send_keys('Elon')
#     last.send_keys('``V')
#     email.send_keys('123abc1234@gmail.com')
#     password.send_keys('12345678mM+$VV')
#     conf_password.send_keys('12345678mM+$VV')
#     button.click()
#     error = driver.find_element(By.XPATH, "(//div[contains(.,'Last Name is not valid!')])[6]")
#     assert error.text == 'Last Name is not valid!'
#
#
# def test_create_account_with_incorrect_flname(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
#     first = driver.find_element(By.ID, 'firstname')
#     last = driver.find_element(By.ID, 'lastname')
#     email = driver.find_element(By.ID, 'email_address')
#     password = driver.find_element(By.ID, 'password')
#     conf_password = driver.find_element(By.ID, 'password-confirmation')
#     button = driver.find_element(By.CSS_SELECTOR, '.submit')
#     first.send_keys('``V')
#     last.send_keys('``V')
#     email.send_keys('123abc1234@gmail.com')
#     password.send_keys('12345678mM+$VV')
#     conf_password.send_keys('12345678mM+$VV')
#     button.click()
#     error = driver.find_element(By.XPATH, "//div[contains(@data-bind,'parent.prepareMessageForHtml(message.text)')]")
#     assert error.text == 'First Name is not valid! Last Name is not valid!'
#
# # ========================================================================
#
# def test_create_account_confirm_password(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
#     first = driver.find_element(By.ID, 'firstname')
#     last = driver.find_element(By.ID, 'lastname')
#     email = driver.find_element(By.ID, 'email_address')
#     password = driver.find_element(By.ID, 'password')
#     conf_password = driver.find_element(By.ID, 'password-confirmation')
#     button = driver.find_element(By.CSS_SELECTOR, '.submit')
#     first.send_keys('Elon')
#     last.send_keys('Mask')
#     email.send_keys('123abc1234@gmail.com')
#     password.send_keys('12345678mM+$VV')
#     conf_password.send_keys('12345678mM+$Vv')
#     button.click()
#     conf_password_error = driver.find_element(By.ID, "password-confirmation-error")
#     assert conf_password_error.text == 'Please enter the same value again.'
#
#
# def test_create_account_with_out_data(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
#     first = driver.find_element(By.ID, 'firstname')
#     last = driver.find_element(By.ID, 'lastname')
#     email = driver.find_element(By.ID, 'email_address')
#     password = driver.find_element(By.ID, 'password')
#     conf_password = driver.find_element(By.ID, 'password-confirmation')
#     button = driver.find_element(By.CSS_SELECTOR, '.submit')
#     first.send_keys('')
#     last.send_keys('')
#     email.send_keys('')
#     password.send_keys('')
#     conf_password.send_keys('')
#     button.click()
#     first_error = driver.find_element(By.ID, 'firstname-error')
#     last_error = driver.find_element(By.ID, 'lastname-error')
#     email_error = driver.find_element(By.ID, 'email_address-error')
#     password_error = driver.find_element(By.ID, 'password-error')
#     conf_password_error = driver.find_element(By.ID, 'password-confirmation-error')
#     assert first_error.text == 'This is a required field.'
#     assert last_error.text == 'This is a required field.'
#     assert email_error.text == 'This is a required field.'
#     assert password_error.text == 'This is a required field.'
#     assert conf_password_error.text == 'This is a required field.'
#
#
# def test_create_account_with_random_data(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
#     first = driver.find_element(By.ID, 'firstname')
#     last = driver.find_element(By.ID, 'lastname')
#     email = driver.find_element(By.ID, 'email_address')
#     password = driver.find_element(By.ID, 'password')
#     button = driver.find_element(By.CSS_SELECTOR, '.submit')
#     first.send_keys('Elon')
#     last.send_keys('Mask')
#
#     email.send_keys('123abc123gmail.com')
#     password.send_keys('1234567')
#     password_error_8_smv = driver.find_element(By.ID, 'password-error')
#     assert password_error_8_smv.text == ('Minimum length of this field must be equal or greater than 8 symbols.'
#                                          ' Leading and trailing spaces will be ignored.')
#
#     password.clear()
#     password.send_keys('12345678')
#     password_error_3_smv = driver.find_element(By.ID, 'password-error')
#     assert password_error_3_smv.text == ('Minimum of different classes of characters in password is 3. '
#                                          'Classes of characters: Lower Case, Upper Case, Digits, Special Characters.')
#
#     password.clear()
#     password.send_keys('12345678mM')
#     password_error_weak = driver.find_element(By.ID, 'password-strength-meter')
#     assert password_error_weak.text == 'Password Strength: Weak'
#
#     password.clear()
#     password.send_keys('12345678mM+$')
#     password_error_medium = driver.find_element(By.ID, 'password-strength-meter')
#     assert password_error_medium.text == 'Password Strength: Medium'
#
#     password.clear()
#     password.send_keys('12345678mM+$VV')
#     password_error_strong = driver.find_element(By.ID, 'password-strength-meter')
#     assert password_error_strong.text == 'Password Strength: Strong'
#
#     button.click()
#
#     email_error = driver.find_element(By.ID, 'email_address-error')
#     assert email_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'
#
#
# #  ============================================================
#
#
# def test_sale_product(driver):
#     driver.get('https://magento.softwaretestingboard.com/sale.html#')
#     jacket = driver.find_element(By.XPATH, "(//a[contains(.,'Jackets')])[3]")
#     jacket.click()
#     title = driver.find_element(By.XPATH, "(//span[contains(.,'Jackets')])[3]")
#     assert title.text == 'Jackets'
#
#
# def test_check_visible_and_clickable_jackets(driver):
#     driver.get("https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html?product_list_order=price")
#     products = driver.find_elements(By.CSS_SELECTOR, "li.product-item")
#     product_count = len(products)
#     expected_count = 12
#     assert product_count == expected_count
#     for index, product in enumerate(products):
#         # проверка видимости и кликабельности с помощью JavaScript
#         is_clickable = driver.execute_script("return arguments[0].offsetParent !== null;", product)
#         assert is_clickable, f"Продукт {index + 1} не кликабелен."
#         print(f"Продукт {index + 1} кликабелен.")
#
#
# def test_sale_bags(driver):
#     driver.get('https://magento.softwaretestingboard.com/sale.html#')
#     bags = driver.find_element(By.XPATH, "(//a[contains(.,'Bags')])[2]")
#     bags.click()
#     title = driver.find_element(By.XPATH, "//span[@data-ui-id='page-title-wrapper']")
#     assert title.text == 'Bags'
#
#
# def test_check_visible_and_clickable_bags(driver):
#     driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
#     products = driver.find_elements(By.CSS_SELECTOR, "li.product-item")
#     product_count = len(products)
#     expected_count = 12
#     assert product_count == expected_count
#     for index, product in enumerate(products):
#         # проверка видимости и кликабельности с помощью JavaScript
#         is_clickable = driver.execute_script("return arguments[0].offsetParent !== null;", product)
#         assert is_clickable, f"Продукт {index + 1} не кликабелен."
#         print(f"Продукт {index + 1} кликабелен.")
#
#
# # =============================================================
#
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import pytest
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
#
# @pytest.fixture()
# def driver():
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     chrome_driver = webdriver.Chrome(options=options)
#     # chrome_driver.implicitly_wait(5)
#     return chrome_driver
#
# def test_sing_in(driver):
#     driver.get('https://magento.softwaretestingboard.com/sale.html')
#     driver.find_element(By.XPATH, "(//a[contains(.,'Sign In')])[1]").click()
#     email = driver.find_element(By.ID, "email")
#     email.send_keys('123abc123abc@gmai.com')
#     password = driver.find_element(By.ID, 'pass')
#     password.send_keys('m96884397$')
#     sing_btn = driver.find_element(By.ID, 'send2')
#     sing_btn.click()
#     WebDriverWait(driver, 3).until(
#         EC.presence_of_all_elements_located((By.XPATH, "(//span[@class='logged-in'])[1]")))
#     welcome = driver.find_element(By.XPATH, "(//span[@class='logged-in'])[1]")
#     assert welcome.text == 'Welcome, Hugo villa!'
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #
# def test_each_product_has_price(driver):
#     driver.get("https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html")
#     products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
#     assert len(products) > 0, "Продукты не найдены на странице."
#     for index, product in enumerate(products, start=1):
#         price_element = product.find_element(By.CSS_SELECTOR, ".price")
#         assert price_element is not None, f"Цена не найдена для продукта {index}."
#         assert price_element.text != "", f"Цена для продукта {index} пуста."
#         print(f"Продукт {index} имеет цену: {price_element.text}")
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_each_product_has_size(driver):
#     driver.get("https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html")
#     products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
#     assert len(products) > 0, "Продукты не найдены на странице."
#     for index, product in enumerate(products, start=1):
#         size_element = product.find_element(By.CSS_SELECTOR, ".swatch-attribute.size")
#         assert size_element is not None, f"Размер не найден для продукта {index}."
#         assert size_element.text != "", f"Размер для продукта {index} пуст."
#         print(f"Продукт {index} имеет размеры: {size_element.text}")
#
# def test_each_product_ha_size(driver):
#     products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
#     assert len(products) > 0, "Продукты не найдены на странице."
#     for index, product in enumerate(products, start=1):
#         size_element = product.find_element(By.CSS_SELECTOR, ".swatch-attribute.size")
#         assert size_element is not None, f"Размер не найден для продукта {index}."
#         assert size_element.text != "", f"Размер для продукта {index} пуст."
#         print(f"Продукт {index} имеет размеры: {size_element.text}")
#
#
#

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск ChromeDriver
driver = webdriver.Chrome()
def test_jhgjhgf():
    # Открытие страницы с коллекцией "Eco-friendly"
    driver.get("https://magento.softwaretestingboard.com/collections/eco-friendly.html")

    # Ожидание загрузки страницы
    time.sleep(5)

    # Проверка наличия заголовка страницы
    title = driver.find_element(By.XPATH, "//h1[@class='page-title']/span")
    assert title.is_displayed(), "Заголовок страницы не отображается"
    assert title.text == "Eco Friendly", "Неверный заголовок страницы"

    # Проверка наличия списка продуктов
    product_list = driver.find_elements(By.XPATH, "//li[contains(@class, 'product-item')]")
    assert len(product_list) > 0, "Список продуктов пуст"

    # Проверка наличия кнопок добавления в корзину
    for product in product_list:
        add_to_cart_button = product.find_element(By.XPATH, ".//button[@title='Add to Cart']")
        assert add_to_cart_button.is_displayed(), f"Кнопка 'Add to Cart' не отображается для продукта: {product.text}"

    # Закрытие браузера
    driver.quit()

