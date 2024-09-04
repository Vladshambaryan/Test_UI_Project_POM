from selenium.webdriver.common.by import By


first_loc = (By.ID, 'firstname')
last_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
conf_password_loc = (By.ID, 'password-confirmation')
button_loc = (By.CSS_SELECTOR, '.submit')

error_loc = (By.XPATH, "(//div[contains(.,'First Name is not valid!')])[6]")
error_ln_loc = (By.XPATH, "(//div[contains(.,'Last Name is not valid!')])[6]")
error_fn_ln_loc = (By.XPATH, "//div[contains(@data-bind,'parent.prepareMessageForHtml(message.text)')]")
conf_password_error_loc = (By.ID, "password-confirmation-error")


#  ========================= password ==========================================

password_message_8_smb_loc = (By.ID, 'password-error')
password_message_3_smb_loc = (By.ID, 'password-error')
password_message_weak_loc = (By.ID, 'password-strength-meter')
password_message_medium_loc = (By.ID, 'password-strength-meter')
password_message_strong_loc = (By.ID, 'password-strength-meter')
email_error_loc = (By.ID, 'email_address-error')
submit_loc = (By.CSS_SELECTOR, '.submit')
