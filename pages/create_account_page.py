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

    def check_error_message_first_name(self):
        error = self.find(locc.error_loc)
        assert error.text == 'First Name is not valid!'

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

    def check_error_message_last_name(self):
        error = self.find(locc.error_ln_loc)
        assert error.text == 'Last Name is not valid!'

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

    def check_error_message_first_and_last_name(self):
        error = self.find(locc.error_fn_ln_loc)
        assert error.text == 'First Name is not valid! Last Name is not valid!'

    def confirm_password(self):
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
        conf_password.send_keys('12345678mM+$Vv')
        button.click()

    def check_confirm_password(self):
        conf_password_error = self.find(locc.conf_password_error_loc)
        assert conf_password_error.text == 'Please enter the same value again.'

    def password_complexity_test(self):
        first = self.find(locc.first_loc)
        last = self.find(locc.last_loc)
        email = self.find(locc.email_loc)
        submit = self.find(locc.submit_loc)
        first.send_keys('Elon')
        last.send_keys('Mask')
        email.send_keys('123abc123gmail.com')

        password = self.find(locc.password_loc)
        password.send_keys('1234567')
        password_message_8_smb = self.find(locc.password_message_8_smb_loc)
        assert password_message_8_smb.text == ('Minimum length of this field must be equal or greater than 8 symbols.'
                                             ' Leading and trailing spaces will be ignored.')

        password.clear()
        password.send_keys('12345678')
        password_message_3_smb = self.find(locc.password_message_3_smb_loc)
        assert password_message_3_smb.text == ('Minimum of different classes of characters in password is 3. '
                                             'Classes of characters: Lower Case, Upper Case, Digits, Special Characters.')

        password.clear()
        password.send_keys('12345678mM')
        password_message_weak = self.find(locc.password_message_weak_loc)
        assert password_message_weak.text == 'Password Strength: Weak'

        password.clear()
        password.send_keys('12345678mM+$')
        password_message_medium = self.find(locc.password_message_medium_loc)
        assert password_message_medium.text == 'Password Strength: Medium'

        password.clear()
        password.send_keys('12345678mM+$VV')
        password_message_strong = self.find(locc.password_message_strong_loc)
        assert password_message_strong.text == 'Password Strength: Strong'

        submit.click()

        email_error = self.find(locc.email_error_loc)
        assert email_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'



