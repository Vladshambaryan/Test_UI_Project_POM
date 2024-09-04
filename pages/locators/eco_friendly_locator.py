from selenium.webdriver.common.by import By


short_loc = (By.XPATH, "//img[@alt='Ana Running Short']")
add_to_cart_loc = (By.XPATH, "//span[contains(.,'Add to Cart')]")
size_loc = (By.ID, "option-label-size-143-item-171")
color_loc = (By.ID, "option-label-color-93-item-56")
view_loc = (By.XPATH, "//span[contains(.,'View and Edit Cart')]")
counter_loc = (By.XPATH, "//span[contains(@class,'counter-number')]")
short1_loc = (By.XPATH, "(//a[contains(.,'Ana Running Short')])[2]")
delete_loc = (By.XPATH, "//a[@href='#'][contains(.,'Remove item')]")



