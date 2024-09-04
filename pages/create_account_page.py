from pages.locators import create_account_locators as locc
from pages.base_page import BasePage


class CreateAccount(BasePage):
    page_url = 'customer/account/create/'

    def incorrect_first_name(self):
        first = self.find(locc.first_loc)
        last = self.find(locc.last_loc)
        email = self.find(locc.email_loc)
        password = self.find(locc.password_loc)
        conf_password = self.find(locc.conf_password_loc)
        button = self.find(locc.button_loc)
        first.send_keys('``V')
        last.send_keys('Mask')
        email.send_keys('123abc1234@gmail.com')
        password.send_keys('12345678mM+$VV')
        conf_password.send_keys('12345678mM+$VV')
        button.click()

    def check_error_message_first_name(self, text):
        error = self.find(locc.error_loc)
        assert error.text == text

    def incorrect_last_name(self):
        first = self.find(locc.first_loc)
        last = self.find(locc.last_loc)
        email = self.find(locc.email_loc)
        password = self.find(locc.password_loc)
        conf_password = self.find(locc.conf_password_loc)
        button = self.find(locc.button_loc)
        first.send_keys('Elon')
        last.send_keys('``V')
        email.send_keys('123abc1234@gmail.com')
        password.send_keys('12345678mM+$VV')
        conf_password.send_keys('12345678mM+$VV')
        button.click()

    def check_error_message_last_name(self, text):
        error = self.find(locc.error_ln_loc)
        assert error.text == text

    def incorrect_first_last_name(self):
        first = self.find(locc.first_loc)
        last = self.find(locc.last_loc)
        email = self.find(locc.email_loc)
        password = self.find(locc.password_loc)
        conf_password = self.find(locc.conf_password_loc)
        button = self.find(locc.button_loc)
        first.send_keys('``V')
        last.send_keys('``V')
        email.send_keys('123abc1234@gmail.com')
        password.send_keys('12345678mM+$VV')
        conf_password.send_keys('12345678mM+$VV')
        button.click()

    def check_error_message_first_and_last_name(self, text):
        error = self.find(locc.error_fn_ln_loc)
        assert error.text == text

    def different_passwords(self):
        first = self.find(locc.first_loc)
        last = self.find(locc.last_loc)
        email = self.find(locc.email_loc)
        password = self.find(locc.password_loc)
        conf_password = self.find(locc.conf_password_loc)
        button = self.find(locc.button_loc)
        first.send_keys('Elon')
        last.send_keys('Mask')
        email.send_keys('123abc1234@gmail.com')
        password.send_keys('12345678mM+$VV')
        conf_password.send_keys('12345678')
        button.click()

    def check_message_confirm_password(self, text):
        conf_password_error = self.find(locc.conf_password_error_loc)
        assert conf_password_error.text == text

    def check_message_weak_password(self, text):
        password = self.find(locc.password_loc)
        password.clear()
        password.send_keys('12345678m')
        password_message_weak = self.find(locc.password_message_weak_loc)
        assert password_message_weak.text == text

    def check_message_medium_password(self, text):
        password = self.find(locc.password_loc)
        password.clear()
        password.send_keys('12345678mM+$')
        password_message_medium = self.find(locc.password_message_medium_loc)
        assert password_message_medium.text == text

    def check_message_strong_password(self, text):
        password = self.find(locc.password_loc)
        password.clear()
        password.send_keys('12345678mM+$VV')
        password_message_strong = self.find(locc.password_message_strong_loc)
        assert password_message_strong.text == text

    def check_message_incorrect_email(self, text):
        email = self.find(locc.email_loc)
        email.send_keys('123abc123gmail.com')
        button = self.find(locc.button_loc)
        button.click()
        email_error = self.find(locc.email_error_loc)
        assert email_error.text == text



