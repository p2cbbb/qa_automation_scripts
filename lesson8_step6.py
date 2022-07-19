from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # Посчитаем математическую функцию от x
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)
    # Скроллим страницу вниз до элемента button
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")
    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_field.send_keys(y)
    # Выбраем checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox.click()
    # Переключаем radiobutton "Robots rule!"
    radio = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radio.click()
    # Нажимаем на кнопку Submit
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
