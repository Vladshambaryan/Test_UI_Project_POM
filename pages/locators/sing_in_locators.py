from selenium.webdriver.common.by import By


sing_loc = (By.XPATH, "(//a[contains(.,'Sign In')])[1]")
email_field_loc = (By.ID, "email")
password_field_loc = (By.ID, 'pass')
sing_btn_loc = (By.ID, 'send2')
welcome_loc = (By.XPATH, "(//span[@class='logged-in'])[1]")
