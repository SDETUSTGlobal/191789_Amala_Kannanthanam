import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

Rediff_HOME = 'https://mail.rediff.com/cgi-bin/login.cgi'

# Scenarios

scenarios('../rediff.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver")
    b.implicitly_wait(10)

    yield b
    b.quit()


# Given Steps

@given('the Rediffmail login page is displayed')
def ddg_home(browser):
    browser.get(Rediff_HOME)


# When Steps

@when(parsers.parse('the user enters the username and password'))
def search_phrase(browser):
    search_input = browser.find_element_by_xpath('//*[@id="login1"]')
    search_input.send_keys('amalak6870052@gmail.com')
    search_pass = browser.find_element_by_name('passwd')
    search_pass.send_keys('test')


@then(parsers.parse('the user click on login'))
def search_product(browser):
    search_pro = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input[2]')
    search_pro.click()