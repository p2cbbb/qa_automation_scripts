from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_field.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radio.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_btn.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()