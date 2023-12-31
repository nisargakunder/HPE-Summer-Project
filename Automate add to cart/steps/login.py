import os
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(filename="amazonlog.log", format="%(asctime)s  %(levelname)s:%(message)s", level=logging.INFO)
screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Screenshots")

def screenshot(driver, filepath):
    if not os.path.exists(screenshot_dir):
        os.mkdir(screenshot_dir)
    driver.save_screenshot(filepath)


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    logging.info("Browser launched")


@when('I visit amazon website')
def step_impl(context):
    try:
        context.driver.get("https://www.amazon.in/")
        logging.info("Opened the website")
    except:
        logging.error("Unable to open website")
        allure.attach("Unable to open website", attachment_type=AttachmentType.TEXT)


@when('Amazon homepage is opened successfully')
def step_impl(context):
    try:
        text = context.driver.title
        assert text == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    except:
        allure.attach("Homepage unavailable", attachment_type=AttachmentType.TEXT) 


@when('I log in with valid phone number or email "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    signin = context.driver.find_element(By.ID, "nav-link-accountList")
    signin.click()
    signin_input = context.driver.find_element(By.ID, "ap_email")
    signin_input.send_keys(user)
    try:
        context.driver.find_element(By.ID, "continue").click()
        pwd_input = context.driver.find_element(By.ID, "ap_password")
        pwd_input.send_keys(pwd)
        context.driver.find_element(By.ID, "signInSubmit").click()
        time.sleep(15)
        try:

            error_message = context.driver.find_element(By.CLASS_NAME, "a-alert-heading").text
            if error_message == "There was a problem":
                screenshot_name2 = "Incorrect_password.png"
                screenshot_path2 = os.path.join(screenshot_dir, screenshot_name2)
                screenshot(context.driver, screenshot_path2)
                print(f"Screenshot saved: {screenshot_path2}")
                allure.attach(context.driver.get_screenshot_as_png(), name="IncorrectPasswordSS", attachment_type=AttachmentType.PNG)
                logging.info("Incorrect password")
                allure.attach("Login failed. Incorrect password", attachment_type=AttachmentType.TEXT)
                context.driver.close()
            elif error_message == "Important Message!":
                time.sleep(20)
                allure.attach(context.driver.get_screenshot_as_png(), name="IncorrectPasswordSS",
                              attachment_type=AttachmentType.PNG)
                context.driver.close()
        except:
            pass
    except NoSuchElementException as e:
        screenshot_name3 = "incorrect_phoneno.png"
        screenshot_path3 = os.path.join(screenshot_dir, screenshot_name3)
        screenshot(context.driver, screenshot_path3)
        allure.attach(context.driver.get_screenshot_as_png(), name="incorrect_phonenoSS", attachment_type=AttachmentType.PNG)
        logging.info("Incorrect mobile number/e-mail ID")
        allure.attach("Login failed. Incorrect mobile number/e-mail ID.", attachment_type=AttachmentType.TEXT)
        context.driver.close()


@when('I should login successfully with "{username}"')
def step_impl(context, username):
    try:
        name1 = context.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").text
        assert name1 == "Hello, {0}".format(username)
        logging.info("Logged in successfully!")
        
    except AssertionError:

        logging.error("Username validation failed.")
        screenshot_name1 = "assertion_error.png"
        screenshot_path1 = os.path.join(screenshot_dir, screenshot_name1)
        screenshot(context.driver, screenshot_path1)
        print(f"Screenshot saved: {screenshot_path1}")
        allure.attach(context.driver.get_screenshot_as_png(), name="AssertionErrorSS",
                      attachment_type=AttachmentType.PNG)
        allure.attach("Username validation failed.", attachment_type=AttachmentType.TEXT)
        raise AssertionError("Login unsuccessful")
