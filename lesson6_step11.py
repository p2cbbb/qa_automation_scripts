from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Ссылка с формой регистрации без бага
    link1 = "http://suninjuly.github.io/registration1.html"
    # Ссылка с формой регистрации с багом
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    # Для запуска автотеста проверки формы с багом поменять link1 на link2
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    # Находим поле ввода имени и заполняем его
    input_first_name = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[1]/input')
    input_first_name.send_keys("Денис")
    # Находим поле ввода фамилии и заполняем его
    input_last_name = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[2]/input')
    input_last_name.send_keys('Антонов')
    # Находим поле ввода email и заполняем его
    input_email = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[3]/input')
    input_email.send_keys('den88ant@yandex.ru')


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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