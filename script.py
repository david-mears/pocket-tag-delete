import os
import time

from selenium import webdriver
from selenium import common
from dotenv import load_dotenv

load_dotenv()
driver = webdriver.Firefox()

# Sign in to LinkedIn and navigate to the desired company's personnel
driver.get('https://app.getpocket.com/tags/hacker-news/all')
time.sleep(3)
username = driver.find_element_by_id('field-1')
username.send_keys(os.getenv("POCKET_USERNAME"))
password = driver.find_element_by_id('field-2')
password.send_keys(os.getenv("POCKET_PASSWORD"))
password.submit()

time.sleep(3)
bulk_edit = driver.find_element_by_css_selector("[aria-label='Bulk Edit']")
bulk_edit.click()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    all_cards = driver.find_elements_by_tag_name("article")

    i = 0
    for card in all_cards:
        try:
            card.click()
        except common.exceptions.ElementClickInterceptedException:
            print("Click intercepted error - selenium.common.exceptions.ElementClickInterceptedException")
            break
        i += 1
        if i == 15:
            break

    delete = driver.find_element_by_css_selector("[aria-label='Delete']")
    delete.click()

    # Confirm deletion
    delete = driver.find_element_by_class_name("css-pfgdmp")
    delete.click()

    # Scroll down to bottom
    driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(1.5)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# Close webdriver
driver.close()