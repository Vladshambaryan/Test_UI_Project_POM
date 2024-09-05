from selenium.webdriver.common.by import By


jacket_loc = (By.XPATH, "(//a[contains(.,'Jackets')])[3]")
page_title_loc = (By.XPATH, "(//span[contains(.,'Jackets')])[3]")
bags_loc = (By.XPATH, "(//a[contains(.,'Bags')])[2]")
title_loc = (By.XPATH, "//span[@data-ui-id='page-title-wrapper']")
products_loc = (By.CSS_SELECTOR, "li.product-item")
products1_loc = (By.CSS_SELECTOR, ".product-item")
product_loc = (By.CSS_SELECTOR, ".price")
prod_loc = (By.CSS_SELECTOR, ".swatch-attribute.size")
