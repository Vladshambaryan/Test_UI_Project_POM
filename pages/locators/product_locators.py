from selenium.webdriver.common.by import By

short_loc = (By.XPATH, "//img[@alt='Ana Running Short']")
size_loc = (By.ID, 'option-label-size-143-item-171')
color_loc = (By.ID, "option-label-color-93-item-56")
count_loc = (By.XPATH, "//span[@class='counter-number']")
add_to_cart_loc = (By.XPATH, "//button[@type='submit'][contains(.,'Add to Cart')]")

color_error_loc = (By.XPATH, "//div[@id='super_attribute[143]-error']")
size_error_loc = (By.XPATH, "//div[@id='super_attribute[93]-error']")
products1_loc = (By.CSS_SELECTOR, "li.product-item")
# reviews_loc = (By.XPATH, "//span[contains(.,'Reviews')]")
# add_reviews_loc = (By.XPATH, "//a[@class='action add']")
# wish_list_loc = (By.XPATH, "(//span[contains(.,'Add to Wish List')])[1]")
compare_loc = (By.XPATH, "(//span[contains(.,'Add to Compare')])[1]")
comparision_list_loc = (By.XPATH, "(//div[contains(.,'You added product Ana Running Short to the comparison list.')])[6]")

product_name_loc = (By.CSS_SELECTOR, "span[data-ui-id='page-title-wrapper']")
product_price_loc = (By.CSS_SELECTOR, "span.price")
available_sizes_loc = (By.CSS_SELECTOR, "div.swatch-attribute.size div.swatch-option")
available_colors_loc = (By.CSS_SELECTOR, "div.swatch-attribute.color div.swatch-option")
