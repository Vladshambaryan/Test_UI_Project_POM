from selenium.webdriver.common.by import By

<<<<<<< HEAD
page_title_loc = (By.XPATH, "(//span[contains(.,'Sale')])[2]")
products_loc = (By.CSS_SELECTOR, "li.product-item")
pands_loc = (By.XPATH, "(//strong[@class='title'])[1]")
mens_loc = (By.XPATH, "(//span[@class='info'])[2]")

=======

jacket_loc = (By.XPATH, "(//a[contains(.,'Jackets')])[3]")
page_title_loc = (By.XPATH, "(//span[contains(.,'Jackets')])[3]")
bags_loc = (By.XPATH, "(//a[contains(.,'Bags')])[2]")
title_loc = (By.XPATH, "//span[@data-ui-id='page-title-wrapper']")
products_loc = (By.CSS_SELECTOR, "li.product-item")
products1_loc = (By.CSS_SELECTOR, ".product-item")
product_loc = (By.CSS_SELECTOR, ".price")
prod_loc = (By.CSS_SELECTOR, ".swatch-attribute.size")
>>>>>>> 7d70dd74a8c026be41e47d614d378dc1523e5b7d
