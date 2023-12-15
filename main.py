import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time

URL = "https://www.luckydoganimalrescue.org/adopt"

def get_dog_data(driver):
    # Get the HTML content after the table is loaded
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')
    dog_rows = soup.select('tr.odd, tr.even') # Selecting all table rows with dogs (one table row = one dog)
    return dog_rows

def filter_to_dog(driver):
    driver.get(URL)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='edit-field-an-species-value']"))
    )
    animal_type_dropdown = driver.find_element(By.XPATH, "//select[@id='edit-field-an-species-value']")
    animal_type_dropdown.click()

    dog_option = driver.find_element(By.XPATH, "//option[@value='Dog']")
    dog_option.click()

    filter_submit_btn = driver.find_element(By.XPATH, "//input[@id='edit-submit-adoptable-animals']")
    filter_submit_btn.click()

    time.sleep(2)

    print(f"Filtered to dog.")

def main():
    driver = webdriver.Safari()

    filter_to_dog(driver)

    dog_list = get_dog_data(driver)

    for dog in dog_list:
        print(dog)
        print("\n")
        print("\n")

    driver.quit()

if __name__ == "__main__":
    main()