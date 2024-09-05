import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_name(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_incorrect_first_name('``V', 'Mask', '123abc1234@gmail.com',
                                                  '12345678mM+$VV', '12345678mM+$VV')
    create_account_page.check_error_message_first_name('First Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_incorrect_last_name('Elon', '``V', '123abc1234@gmail.com',
                                                 '12345678mM+$VV', '12345678mM+$VV')
    create_account_page.check_error_message_last_name('Last Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_incorrect_first_last_name('Elon', 'Mask', '123abc1234@gmail.com',
                                                       '12345678mM+$VV', '12345678mM+$VV')
    create_account_page.check_error_message_first_and_last_name('First Name is not valid! Last Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_validation_confirm_password(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_different_password('Elon', 'Mask', '123abc1234@gmail.com',
                                                '12345678mM+$VV', '12345678mM+$Vv')
    create_account_page.check_message_confirm_password('Please enter the same value again.')


@pytest.mark.regression
def test_password_complexity(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_incorrect_email('123abc123gmail.com')
    create_account_page.check_message_incorrect_email('Please enter a valid email address (Ex: johndoe@domain.com).')
    create_account_page.fill_weak_password('12345678m')
    create_account_page.check_message_weak_password('Password Strength: Weak')
    create_account_page.fill_medium_password('12345678mM+$')
    create_account_page.check_message_medium_password('Password Strength: Medium')
    create_account_page.fill_strong_password('12345678mM+$VV')
    create_account_page.check_message_strong_password('Password Strength: Strong')
