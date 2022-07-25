from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def test_registration(link):
    browser = webdriver.Chrome()
    browser.get(link)
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
    return welcome_text

class TestSelectors(unittest.TestCase):
    def test_form_without_bug(self):
        # Ссылка с формой регистрации без бага
        link = "http://suninjuly.github.io/registration1.html"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", test_registration(link), "Expected text not equal real text")
        
    def test_form_with_bug(self):
        # Ссылка с формой регистрации с багом
        link = "http://suninjuly.github.io/registration2.html"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertNotEqual("Congratulations! You have successfully registered!", test_registration(link), "Expected text equal real text")
        
if __name__ == "__main__":
    unittest.main()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    TestSelectors.browser.quit()
