from selenium.webdriver.common.by import By


#  ============================ sale page =====================
jacket_loc = (By.XPATH, "(//a[contains(.,'Jackets')])[3]")
page_title_loc = (By.XPATH, "(//span[contains(.,'Jackets')])[3]")
bags_loc = (By.XPATH, "(//a[contains(.,'Bags')])[2]")
title_loc = (By.XPATH, "//span[@data-ui-id='page-title-wrapper']")
products_loc = (By.CSS_SELECTOR, "li.product-item")
products1_loc = (By.CSS_SELECTOR, ".product-item")
product_loc = (By.CSS_SELECTOR, ".price")
prod_loc = (By.CSS_SELECTOR, ".swatch-attribute.size")

#  ========================= add to cart =====================

short_loc = (By.XPATH, "//img[@alt='Ana Running Short']")
size_loc = (By.ID, 'option-label-size-143-item-171')
color_loc = (By.ID, "option-label-color-93-item-56")
add_cart_loc = (By.XPATH, "//span[contains(.,'Add to Cart')]")
item_in_cart_loc = (By.XPATH, "//a[contains(.,'Ana Running Short')]")
count_loc = (By.XPATH, "(//span[contains(@class,'counter qty')])[1]")

select_size_loc = (By.XPATH, "//div[@id='super_attribute[93]-error']")
select_color_loc = (By.XPATH, "//div[@id='super_attribute[143]-error']")

delete_loc = (By.XPATH, "//a[@href='#'][contains(.,'Remove')]")
alert_ok_loc = (By.XPATH, "//span[contains(.,'OK')]")
