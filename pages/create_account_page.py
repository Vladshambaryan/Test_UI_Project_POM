from pages.locators import create_account_locators as locc
from pages.base_page import BasePage


class CreateAccount(BasePage):

    account_create_page_url = 'customer/account/create/'

    def fill_incorrect_data(self,  first, last, email, password, conf_password):
        first_field = self.find(locc.first_loc)
        last_field = self.find(locc.last_loc)
        email_field = self.find(locc.email_loc)
        password_field = self.find(locc.password_loc)
        conf_password_field = self.find(locc.conf_password_loc)
        button = self.find(locc.button_loc)
        first_field.send_keys(first)
        last_field.send_keys(last)
        email_field.send_keys(email)
        password_field.send_keys(password)
        conf_password_field.send_keys(conf_password)
        button.click()

    def check_error_message_first_name(self, text):
        error = self.find(locc.error_loc)
        assert error.text == text

    def check_error_message_last_name(self, text):
        error = self.find(locc.error_ln_loc)
        assert error.text == text

    def check_error_message_first_and_last_name(self, text):
        error = self.find(locc.error_fn_ln_loc)
        assert error.text == text

    def fill_incorrect_email(self, email):
        email_field = self.find(locc.email_loc)
        email_field.send_keys(email)
        button = self.find(locc.button_loc)
        button.click()

    def check_message_incorrect_email(self, text):
        email_error = self.find(locc.email_error_loc)
        assert email_error.text == text

    def check_message_confirm_password(self, text):
        conf_password_error = self.find(locc.conf_password_error_loc)
        assert conf_password_error.text == text

    def fill_weak_password(self, password):
        password_field = self.find(locc.password_loc)
        password_field.clear()
        password_field.send_keys(password)

    def check_message_weak_password(self, text):
        password_message_weak = self.find(locc.password_message_weak_loc)
        assert password_message_weak.text == text

    def fill_medium_password(self, password):
        password_field = self.find(locc.password_loc)
        password_field.clear()
        password_field.send_keys(password)

    def check_message_medium_password(self, text):
        password_message_medium = self.find(locc.password_message_medium_loc)
        assert password_message_medium.text == text

    def fill_strong_password(self, password):
        password_field = self.find(locc.password_loc)
        password_field.clear()
        password_field.send_keys(password)

    def check_message_strong_password(self, text):
        password_message_strong = self.find(locc.password_message_strong_loc)
        assert password_message_strong.text == text
