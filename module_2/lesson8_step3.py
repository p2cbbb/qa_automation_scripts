from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим два числа и складываем их
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    total = str(int(num1.text) + int(num2.text))
    print(total)


    # Открываем выпадающий список и находим нужный ответ
    browser.find_element(By.CSS_SELECTOR, "select#dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{total}']").click()

    # Отправляем ответ
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_btn.click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()