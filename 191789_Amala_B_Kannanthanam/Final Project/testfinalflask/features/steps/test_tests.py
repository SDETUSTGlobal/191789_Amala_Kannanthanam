import time
import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

TEST_HOME = 'http://127.0.0.1:5000/'

# Scenarios

scenarios('../test.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver")
    b.implicitly_wait(10)
    b.maximize_window()

    yield b
    b.quit()


# Given Steps

@given('the localhost is displayed')
def ddg_home(browser):
    browser.get(TEST_HOME)


# When Steps

@when(parsers.parse('the user enters the details'))
def search_phrase(browser):
    search_input = browser.find_element_by_id('name')
    search_input.send_keys('Alisha')
    time.sleep(2)
    search_pass = browser.find_element_by_id('lastname')
    search_pass.send_keys('Thomas')
    time.sleep(2)
    search_uid = browser.find_element_by_id('uid')
    search_uid.send_keys('567899')
    time.sleep(2)
    search_company= browser.find_element_by_id('company')
    search_company.send_keys('Qtech')
    time.sleep(2)
    search_email = browser.find_element_by_id('email')
    search_email.send_keys('alisha@gmail.com')
    time.sleep(2)
    search = browser.find_element_by_xpath('//*[@id="abc"]/button')
    search.click()
    time.sleep(10)

@then(parsers.parse('the user details are shown'))
def found():
    print("\nTEST SUCCESSFUL")



