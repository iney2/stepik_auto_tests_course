from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
# people_radio = browser.find_element(By.CSS_SELECTOR, '#peopleRule')
# people_checked = people_radio.get_attribute("checked")

# print("value of people radio: ", people_checked)
#assert robots_checked is None

try:
    treasure = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = treasure.get_attribute("valuex")
    print(x)
    #x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    #x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    Checkbox1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    Checkbox1.click()
    Radio1 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    Radio1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
