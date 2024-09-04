import pytest


@pytest.mark.regression
def test_sing_in_page(login_page):
    login_page.open_page()
    login_page.sing_in_click()
    login_page.fill_login_form('123abc123abc@gmai.com', 'm96884397$')
    login_page.check_text_is('Welcome, Hugo villa!')
