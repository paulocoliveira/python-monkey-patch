from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import pytest
import os
from time import sleep

@pytest.fixture(params=["chrome-Windows11", "firefox-macOSVentura"],scope="class")
def driver(request):
    username = os.getenv("LT_USERNAME")
    accessToken = os.getenv("LT_ACCESS_KEY")
    gridUrl = "hub.lambdatest.com/wd/hub"

    if request.param == "chrome-Windows11":
        web_driver = webdriver.ChromeOptions()
        platform = "Windows 11"
    if request.param == "firefox-macOSVentura":
        web_driver = webdriver.FirefoxOptions()
        platform = "MacOS Ventura"

    lt_options = {
        "user": username,
        "accessKey": accessToken,
        "build": "monkey patching build",
        "name": "monkey patching test",
        "platformName": platform,
        "w3c": True,
        "browserName": "Chrome",
        "browserVersion": "latest",
        "selenium_version": "4.8.0",
    }
    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = "https://"+username+":"+accessToken+"@"+gridUrl
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

def custom_click(self):
    # Perform additional actions before clicking
    sleep(10)
    
    # Call the original click() method
    self._original_click()

# Patching the WebElement class with the custom_click() method
WebElement._original_click = WebElement.click
WebElement.click = custom_click

def test_simple_demo_form(driver):
    # Load a webpage
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("This is a monkey patching text!")

    # Find an element by its ID and click on it
    element = driver.find_element(By.ID, "showInput")
    element.click()

    # Find an element by its ID and extract its text
    element = driver.find_element(By.ID, "message")
    assert element.text == "This is a monkey patching text!"