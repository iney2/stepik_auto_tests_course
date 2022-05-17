from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:


    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Name")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("LastName")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("Email")

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys('C:\\Users\\ep\\selenium_course\\file.txt')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Отправляем заполненную форму
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
