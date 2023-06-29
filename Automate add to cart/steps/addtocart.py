from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'User launches Google Chrome web browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(90)


@given('User opens www.amazon.in')
def step_impl(context):
    context.driver.get("https://www.amazon.in")
    context.driver.get(r"https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

@when('user enters mobile number "{mobileno}"')
def step_impl(context, mobileno):
    context.driver.find_element(By.ID, "ap_email").send_keys(mobileno)
    continue_button = context.driver.find_element(By.ID, "continue")
    continue_button.click()


@when('user enters password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "ap_password").send_keys(password)
    continue_button = context.driver.find_element(By.ID, "continue")
    continue_button.click()


@then(u'User searches for required item')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("SONY 55inch TV")
    context.driver.find_element(By.ID, 'nav-search-submit-button').click() #click on the search icon


@then(u'Clicks on the desired item')
def step_impl(context):
    context.driver.execute_script("""window.open('https://www.amazon.in/Sony-Bravia-inches-Google-KD-55X74K/dp/B09WN26DG5/ref=sr_1_3?crid=Q4MO3BD2PSZG&keywords=SONY+55inch+TV&qid=1687795413&sprefix=sony+55inch+tv%2Caps%2C500&sr=8-3', '_blank');""")
    context.driver.switch_to.window(window_name=context.driver.window_handles[-1])


@then(u'Adds the item to the shopping cart')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(10)