from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Нажимаем на кнопку и переключаемся на новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Посчитаем математическую функцию от x
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)
    # Скроллим страницу вниз до элемента button
    button_submit = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")
    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_field.send_keys(y)
    # Нажимаем на кнопку Submit
    button_submit.click()

    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
