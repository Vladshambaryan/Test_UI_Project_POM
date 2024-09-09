from selenium.webdriver.common.by import By

short_loc = (By.XPATH, "//img[@alt='Ana Running Short']")
size_loc = (By.ID, 'option-label-size-143-item-171')
color_loc = (By.ID, "option-label-color-93-item-56")
count_loc = (By.XPATH, "//span[@class='counter-number']")
add_to_cart_loc = (By.XPATH, "//button[@type='submit'][contains(.,'Add to Cart')]")

color_error_loc = (By.XPATH, "//div[@id='super_attribute[143]-error']")
size_error_loc = (By.XPATH, "//div[@id='super_attribute[93]-error']")