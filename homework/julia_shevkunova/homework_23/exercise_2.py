from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)
    chrome_driver.quit()


def test_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    wait = WebDriverWait(driver, 10)

    # Текстовые поля
    driver.find_element(By.ID, 'firstName').send_keys('firstName')
    driver.find_element(By.ID, 'lastName').send_keys('lastName')
    driver.find_element(By.ID, 'userEmail').send_keys('name@example.com')

    # Gender
    gender_label = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    ActionChains(driver).move_to_element(gender_label).click().perform()

    # Phone
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')

    # DOB
    dob_input = driver.find_element(By.ID, 'dateOfBirthInput')
    ActionChains(driver).move_to_element(dob_input).click().perform()
    dob_input.send_keys('17 Nov 2020')
    dob_input.send_keys(Keys.ENTER)

    # Subjects
    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys('Arts')
    subjects.send_keys(Keys.ENTER)
    subjects.click()

    # Hobbies
    hobby_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="hobbies-checkbox-1"]')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hobby_label)
    ActionChains(driver).move_to_element(hobby_label).pause(0.2).click().perform()

    # Address
    driver.find_element(By.ID, 'currentAddress').send_keys('My address')

    # Scroll to State/City
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # STATE
    state_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-select-3-input')))
    state_input.send_keys('N'[0])  # первая буква N
    state_input.send_keys(Keys.ENTER)

    # CITY
    city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-select-4-input')))
    city_input.send_keys('D'[0])  # первая буква D
    city_input.send_keys(Keys.ENTER)

    # Submit
    submit_btn = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()

    modal = driver.find_element(By.XPATH, '//div[@class="modal-content"]')
    print(modal.text)
