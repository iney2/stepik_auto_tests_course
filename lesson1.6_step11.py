from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
try:


    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block [placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block [placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block [placeholder="Input your email"]')
    input3.send_keys("test@test.test")
    input4 = browser.find_element(By.CSS_SELECTOR, '.second_block [placeholder="Input your phone:"]')
    input4.send_keys("555555555")
    input4 = browser.find_element(By.CSS_SELECTOR, '.second_block [placeholder="Input your address:"]')
    input4.send_keys("test address")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()