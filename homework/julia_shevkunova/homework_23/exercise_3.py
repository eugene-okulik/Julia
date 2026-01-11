from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(2)
    chrome_driver.quit()


def test_form(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")

    # Select language
    select = Select(driver.find_element(By.ID, "id_choose_language"))
    select.select_by_visible_text("Python")

    selected_language = select.first_selected_option.text

    # Submit
    submit_btn = driver.find_element(By.NAME, "submit")
    submit_btn.click()

    # Result
    result = driver.find_element(By.ID, "result-text")
    assert result.text == selected_language

def test_form_second(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    submit_btn = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    submit_btn.click()
    result = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "finish"))
       )
    assert result.text == "Hello World!"
