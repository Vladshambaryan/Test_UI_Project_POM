import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_name(create_account_page):
    create_account_page.open_page()
    create_account_page.incorrect_first_name()
    create_account_page.check_error_message_first_name()


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.incorrect_last_name()
    create_account_page.check_error_message_last_name()


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_last_name(create_account_page):
    create_account_page.open_page()
    create_account_page.incorrect_first_last_name()
    create_account_page.check_error_message_first_and_last_name()


@pytest.mark.negative
@pytest.mark.regression
def test_validation_confirm_password(create_account_page):
    create_account_page.open_page()
    create_account_page.confirm_password()
    create_account_page.check_confirm_password()


@pytest.mark.regression
def test_password_complexity(create_account_page):
    create_account_page.open_page()
    create_account_page.password_complexity_test()
























