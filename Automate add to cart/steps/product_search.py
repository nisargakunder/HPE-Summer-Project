import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import logging
import allure
from allure_commons.types import AttachmentType

logging.basicConfig(filename="amazonlog.log", format="%(asctime)s  %(levelname)s:%(message)s", level=logging.INFO)

current_dir = os.path.dirname(os.path.realpath(__file__))
screenshot_dir = os.path.join(current_dir, "screenshots")


@when('search for the "{product}"')
def step_impl(context,product):
    try:
        context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(product)
        logging.info("Searched for the product")
    except:
        logging.info("Couldn't locate search box")


@when('click on search button')
def step_impl(context):
    try:
        context.driver.find_element(By.ID,"nav-search-submit-button").click()
        logging.info("Clicked on search button")
    except:
        assert "No results for" in context.driver.page_source
        time.sleep(10)
        screenshot_path3 = os.path.join(screenshot_dir, "unsuccessful_search.png")
        context.driver.save_screenshot(screenshot_path3)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)


@then('find the third product')
def step_impl(context):
    try:
        window_before=context.driver.window_handles[0]
        try:
            context.driver.find_element("xpath","//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").click()
        except NoSuchElementException:
            logging.info("Couldn't locate the product")
            allure.attach("Couldn't locate the product", attachment_type=AttachmentType.TEXT)
        time.sleep(5)
        window_after=context.driver.window_handles[1]
        context.driver.switch_to.window(window_after)
        logging.info("Opened the product on a new tab")
    except Exception as e:
        logging.error("Couldn't open new tab")
        allure.attach("Couldn't open new tab", attachment_type=AttachmentType.TEXT)
        raise e
