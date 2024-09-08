from selenium.webdriver.common.by import By

page_title_loc = (By.XPATH, "(//span[contains(.,'Sale')])[2]")
products_loc = (By.CSS_SELECTOR, "li.product-item")
pands_loc = (By.XPATH, "(//strong[@class='title'])[1]")
mens_loc = (By.XPATH, "(//span[@class='info'])[2]")

