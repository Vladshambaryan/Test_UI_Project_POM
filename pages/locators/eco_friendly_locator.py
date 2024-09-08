from selenium.webdriver.common.by import By


price_filter_loc = (By.XPATH, "(//div[contains(.,'Price')])[13]")
product_loc = (By.CSS_SELECTOR, ".price")
products_loc = (By.CSS_SELECTOR, "li.product-item")
price_range_loc = (By.XPATH, "//span[contains(.,'$29.99')]")
filtered_loc = (By.XPATH, "(//p[@id='toolbar-amount'])[1]")
search_results_loc = (By.XPATH, "(//p[contains(.,'3 Items')])[1]")
sort_select_loc = (By.XPATH, "//select[@id='sorter']")
products1_loc = (By.CSS_SELECTOR, "li.product-item")
product_element_loc = (By.CSS_SELECTOR, "div.product-item-info .product-item-name")
product_elements_loc = (By.CSS_SELECTOR, "div.product-item-info .swatch-attribute.size .swatch-option")



