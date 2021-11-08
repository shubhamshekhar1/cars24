import time
from MailReader import *

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import config_file_reader
# import header_initialisation
from behave import given, when, then

# headers = header_initialisation.price_fetch_headers
# url = config_file_reader.price_fetch_url
# r = requests.get('https://www.google.com')


# password = otp.read_email_from_gmail()

login_sign_up = "//a[text()='Login / Sign Up']"
facebook_log_in_option = "//button[text()='Continue with Facebook']"
facebook_email_textbox = "//input[@name='email']"
email_id = "shekhartest123@rediffmail.com"
facebook_password_textbox = "//input[@name='pass']"
password = "Cars@24"
facebook_log_in_button = "//input[@name='login']"


@given('visit url "{url}" and login with facebook')
def step(context, url):
    # context.browser.delete_all_cookies()
    context.browser.get(url)
    time.sleep(3)
    context.browser.maximize_window()
    context.browser.find_element_by_xpath(login_sign_up).click()
    time.sleep(2)
    window_before = context.browser.window_handles[0]
    context.browser.find_element_by_xpath(facebook_log_in_option).click()
    time.sleep(5)
    window_after = context.browser.window_handles[1]
    context.browser.switch_to_window(window_after)
    context.browser.find_element_by_xpath(facebook_email_textbox).send_keys(email_id)
    time.sleep(1)
    context.browser.find_element_by_xpath(facebook_password_textbox).send_keys(password)
    time.sleep(1)
    context.browser.find_element_by_xpath(facebook_log_in_button).click()
    time.sleep(5)
    context.browser.switch_to_window(window_before)


""""@then('check title')
def step(context):
    print(context.browser.title)
    assert context.browser.title == "Buy Quality Cars Online. Free Home Delivery. 6 Month Warranty. CARS24 Australia"
    """

"""@when('Passing make value "{make}" and "{model}"')
def step(context, make, model):
    context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/section[1]/div[2]/div[2]/div[1]/div/div").click()
    time.sleep(2)
    ele1= context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/section[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[1]")
    ele1.send_keys(make)
    context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/section[1]/div[2]/div[2]/div[2]/div/div").click()
    time.sleep(2)
    ele2= context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/section[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]")
    ele2.send_keys(model)"""


@then('clicking on show me')
def step(context):
    context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/section[1]/div[2]/div[2]/button").click()
    time.sleep(3)


@when('User clicks on get started')
def step(context):
    context.browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/div/div[4]/button").click()
    time.sleep(3)


@given('User clicks on one car')
def step(context):
    context.browser.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div/div/div[4]/div/div[2]/a/div[2]/div[1]/h2").click()
    time.sleep(3)


@when('User clicks on find a car')
def step(context):
    context.browser.find_element_by_xpath('//a[@data-event="find_car"]').click()
    time.sleep(2)


@then('User clicks on one car')
def step(context):
    context.browser.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div/div/div[4]/div/div[2]/a/div[2]/div[1]/h2").click()
    time.sleep(2)


@when('Passing make value "{make}" and "{model}"')
def step(context, make, model):
    action = ActionChains(context.browser)

    ele1 = context.browser.find_element_by_xpath('//div[text()="Select Make"]')
    action.click(on_element=ele1).send_keys(make + Keys.TAB).perform()
    # ele1.send_keys(make)
    time.sleep(2)

    ele2 = context.browser.find_element_by_xpath('//div[text()="Select Model"]')
    action.click(on_element="ele2")
    # ele2.send_keys(model)


@when('user clicks on login')
def step(context):
    action1: ActionChains(context.browser)

    context.browser.find_element_by_xpath("//a[text()='Login / Sign Up']").click()
    time.sleep(2)
    google_button = context.browser.find_element_by_xpath('//img[@alt="Sign in with Google"]')
    window_before = context.browser.window_handles[0]

    ActionChains(context.browser).key_down(Keys.CONTROL).click(google_button).key_up(Keys.CONTROL).perform()
    time.sleep(5)
    window_after = context.browser.window_handles[1]
    context.browser.switch_to_window(window_after)
    time.sleep(2)
    context.browser.find_element_by_xpath("//input[@type='email']").send_keys("iamshekhuss@gmail.com")
    time.sleep(2)
    context.browser.find_element_by_xpath("//span[text()='Next']").click()
    time.sleep(3)
    context.browser.find_element_by_xpath("//span[text()='Try again']").click()
    time.sleep(3)
    context.browser.find_element_by_xpath("//input[@type='email']").send_keys("iamshekhuss@gmail.com")
    time.sleep(2)
    context.browser.find_element_by_xpath("//span[text()='Next']").click()
    time.sleep(3)
    context.browser.find_element_by_xpath("//input[@type='password']").send_keys("mainahibtaunga")
    time.sleep(2)
    context.browser.find_element_by_xpath("//span[text()='Next']").click()
    time.sleep(2)


show_me_button = "//button[text()='Show Me']"
any_car = "/html/body/div[1]/div[2]/div[4]/div/div/div[4]/div/div[2]/a/div[2]/div[1]/h2"
get_started_button = "/html/body/div[2]/div[4]/div[2]/div[2]/div/div[4]/button"
first_name_textbox = '//input[@id="firstName"]'
last_name_textbox = '//input[@id="lastName"]'
phone_number_textbox = '//input[@id="phone"]'
next_button = '//button[text()="Next"]'
google_address_box = '/html/body/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]'
split_full_payment_option = '//img[@src="https://www.cars24.com/au/static/js/38dd99d8a43d37d0422b33d29276f7c8.svg"]'
i_dont_have_trade_in_button = '//span[text()="I DON’T HAVE A TRADE-IN"]'
partial_payment_radio = '/html/body/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div'
slider_circle = '//div[contains(@class,"sliderCircle")]'
proceed_button = '//button[contains(text(),"PROCEED")]'


@when('clicking on show me and clicks on one car')
def step(context):
    context.browser.find_element_by_xpath(show_me_button).click()
    time.sleep(1)
    context.browser.find_element_by_xpath(any_car).click()
    time.sleep(1)
    context.browser.find_element_by_xpath(get_started_button).click()
    time.sleep(1)
    context.browser.find_element_by_xpath(first_name_textbox).clear()
    context.browser.find_element_by_xpath(first_name_textbox).send_keys("FirstTest")
    time.sleep(1)
    context.browser.find_element_by_xpath(last_name_textbox).clear()
    context.browser.find_element_by_xpath(last_name_textbox).send_keys("LastTest")
    time.sleep(1)
    context.browser.find_element_by_xpath(phone_number_textbox).clear()
    context.browser.find_element_by_xpath(phone_number_textbox).send_keys("478982622")
    time.sleep(1)
    context.browser.find_element_by_xpath(next_button).click()
    time.sleep(2)
    ele = context.browser.find_element_by_xpath(google_address_box)

    ActionChains(context.browser).click(ele).send_keys("3000").pause(2).key_down(Keys.ENTER).key_up(
        Keys.ENTER).perform()
    time.sleep(1)
    context.browser.find_element_by_xpath(next_button).click()
    time.sleep(1)
    context.browser.find_element_by_xpath(i_dont_have_trade_in_button).click()
    time.sleep(2)
    context.browser.find_element_by_xpath(split_full_payment_option).click()
    time.sleep(2)
    context.browser.find_element_by_xpath(partial_payment_radio).click()
    time.sleep(2)
    slider = context.browser.find_element_by_xpath(slider_circle)
    ActionChains(context.browser).drag_and_drop_by_offset(slider, 30, 0).perform()
    time.sleep(5)
    context.browser.find_element_by_xpath(proceed_button).click()
    time.sleep(2)

    # context.browser.find_element_by_xpath('//button[text()="Next"]').click()
    # time.sleep(2)

#
# @given('Create the header & url based on appointment id')
# def step(context):
#     global headers
#     global url
#     print("In the fn Create the header & url based on appointment id")
#     #url = 'https://listing-service-au.c24.tech/v1/vehicle/pricing/6111223748'
#
#
# @when('Perform the get call on price fetch api')
# def enter_item_name(context):
#     global r
#     global headers
#     global url
#     print("In the fn Perform the get call on price fetch api")
#     r = requests.get(url, data=None, headers=headers)
#
#
# @then('Validate the status code & price')
# def see_login_message(context):
#     global r
#     print("In the fn Validate the status code & price")
#     print("API response time is: ", r.elapsed.total_seconds())
#     print(r.json())
#     assert r.status_code == 200, "Response code is not 200"
#     assert r.json()[0]['egc'] == r.json()[1]['egc'] == r.json()[2]['egc'], "EGC value is different in all the states"
#
#
