from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
# Ожидание каждого элемента в течение 5 секунд:
browser.implicitly_wait(5)

try:
    browser.get("http://suninjuly.github.io/wait2.html")

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()