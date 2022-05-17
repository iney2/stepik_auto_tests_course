from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# Wait the element in 5 sec
browser.implicitly_wait(5)

try:
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(3)
    # close the browser
    browser.quit()
