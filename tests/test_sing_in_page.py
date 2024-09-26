import pytest


@pytest.mark.regression
def test_sing_in_page(login_page):
    login_page.open_login_page()
    login_page.sing_in_click()
    login_page.fill_login_form('123abc123abc@gmai.com', 'm96884397$')
    login_page.check_text_is('Welcome, UpdatedName User!')


@pytest.mark.negative
def test_sing_in_page(login_page):
    login_page.open_login_page()
    login_page.sing_in_click()
    login_page.fill_login_form('123abc123abc@gmai.com', 'm96')
    login_page.check_error_text('The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')
