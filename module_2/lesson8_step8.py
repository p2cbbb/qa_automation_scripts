from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Заполняем текстовые поля: имя, фамилия, email
    input_firstname = browser.find_element(By.NAME, 'firstname')
    input_firstname.send_keys('Denis')
    input_lastname = browser.find_element(By.NAME, 'lastname')
    input_lastname.send_keys('Antonov')
    input_email = browser.find_element(By.NAME, 'email')
    input_email.send_keys('den88ant@yandex.ru')

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    input_file = browser.find_element(By.ID, 'file')
    input_file.send_keys(file_path)

    # Нажимаем на кнопку Submit
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
