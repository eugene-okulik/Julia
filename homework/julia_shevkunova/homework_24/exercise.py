from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_adding_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # 1. открыть сайт
    driver.get("http://testshop.qa-practice.com/")

    # 2. перейти в категорию Desks
    driver.find_element(
        By.CSS_SELECTOR,
        'li[data-link-href="/shop/category/desks-1"]'
    ).click()

    # 3. найти товар
    product = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href*="customizable-desk"]')
    ))

    # 4. открыть товар в новой вкладке
    driver.execute_script("window.open(arguments[0]);", product.get_attribute("href"))
    # 5. переключиться на новую вкладку
    driver.switch_to.window(driver.window_handles[1])

    # 6. нажать "Add to cart"
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add_to_cart")
    )).click()

    # 7. нажать на Continue Shopping в popup
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='Continue Shopping']")
    )).click()

    # 8. перейти в корзину
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/cart"]').click()
    # 9. проверить товар в корзине
    cart_product = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h6[contains(text(), 'Customizable Desk')]")
    ))

    assert "Customizable Desk" in cart_product.text


def test_adding_from_shopping_cart_icon(driver):
    wait = WebDriverWait(driver, 10)

    # 1. открыть сайт
    driver.get("http://testshop.qa-practice.com/")

    # 2. найти товар
    product = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".oe_product_cart")
    ))

    # 3. взять название товара
    product_name = product.text

    # 4. навести мышку
    ActionChains(driver).move_to_element(product).perform()
    # 5. нажать на корзину
    add_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a.a-submit[aria-label='Shopping cart']")
    ))
    add_btn.click()

    # 6. дождаться появления popup
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".modal-content")
    ))

    # 7. проверить, что товар есть в popup
    cart_item = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Customizable Desk')]")
    ))

    assert "Customizable Desk" in cart_item.text
