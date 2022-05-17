from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math


def calc(a, b):
    return int(a)+int(b)


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = b_element.text
    y = calc(a, b)
    print(y)

    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))  # ищем элемент в списке со значением y

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
