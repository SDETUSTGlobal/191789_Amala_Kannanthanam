from behave import *
from selenium import webdriver

@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
@when('open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify logo is present on the page')
def step_impl(context):
    status=context.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/img").is_displayed()
    assert status is True


@then('close browser')
def step_impl(context):
  context.driver.close()
