from time import sleep

from pages.locators import sing_in_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    login_page_url = 'customer/account/login'

    def fill_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        sing_btn = self.find(loc.sing_btn_loc)
        email_field.send_keys(login)
        password_field.send_keys(password)
        sing_btn.click()

    def sing_in_click(self):
        sing = self.find(loc.sing_loc)
        sing.click()

    def check_text_is(self, text):
        sleep(3)
        WebDriverWait(self.driver, 6).until(
            EC.presence_of_all_elements_located((By.XPATH, "(//span[@class='logged-in'])[1]")))
        welcome = self.find(loc.welcome_loc)
        assert welcome.text == text
        print(welcome.text)

    def check_error_text(self, text):
        sleep(3)
        welcome = self.driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
        sleep(1)
        assert welcome.text == text

