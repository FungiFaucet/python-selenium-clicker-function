from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException

import time



# Selenium Setup:
serv_obj = Service("C:/Users/vinyl/Documents/SeleniumWebDrivers/SeleniumWebDriversUnzipped/chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("user-data-dir=/path/to/your/custom/profile")
# ops.add_argument('--headless')
# ops.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=serv_obj, options=option)
driver.implicitly_wait(30)
actions = ActionChains(driver)


def link_click(locator_type, search, description):
    locator_map = {
        'XPATH': By.XPATH,
        'CLASS': By.CLASS_NAME,
        'ID': By.ID,
        # Add other locators as needed
    }

    locator = locator_map.get(locator_type.upper())

    if locator is None:
        raise ValueError(f"Invalid locator type: {locator_type}")

    attempt = 0
    attempts = 60
    error_message = f"{description} not found. Attempt:{attempt} waiting 1 second"

    for attempt in range(attempts):
        try:
            driver.find_element(locator, search).click()
            break
        except (ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException):
            print(error_message)
            time.sleep(1)

driver.get('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiA_M21wIn-AhX6mWoFHXadA1EQPAgJ')

time.sleep(1)

link_click('XPATH', "//a[@aria-label='Gmail (opens a new tab)']", 'gmail button')

