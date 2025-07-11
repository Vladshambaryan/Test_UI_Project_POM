from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.create_account_page import CreateAccount
from pages.sing_in import LoginPage
from pages.ana_running_short_page import AnaRunningShort
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendly
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(7)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def ana_running_short_page(driver):
    return AnaRunningShort(driver)
