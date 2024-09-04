import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_name(create_account_page):
    create_account_page.open_page()
    create_account_page.incorrect_first_name()
    create_account_page.check_error_message_first_name('First Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.incorrect_last_name()
    create_account_page.check_error_message_last_name('Last Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.incorrect_first_last_name()
    create_account_page.check_error_message_first_and_last_name('First Name is not valid! Last Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_validation_confirm_password(create_account_page):
    create_account_page.open_page()
    create_account_page.different_passwords()
    create_account_page.check_message_confirm_password('Please enter the same value again.')


@pytest.mark.regression
def test_password_complexity(create_account_page):
    create_account_page.open_page()
    create_account_page.check_message_incorrect_email('Please enter a valid email address (Ex: johndoe@domain.com).')
    create_account_page.check_message_weak_password('Password Strength: Weak')
    create_account_page.check_message_medium_password('Password Strength: Medium')
    create_account_page.check_message_strong_password('Password Strength: Strong')
























