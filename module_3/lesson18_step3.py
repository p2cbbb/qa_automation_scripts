import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898',
                                    '236899', '236903', '236904', '236905'])
def test_solve_stepik_problem(browser, lesson):
    # вычисляем правильный ответ
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    # открываем страницу
    browser.get(link)
    browser.implicitly_wait(5)
    # вводим ответ в поле ответа
    browser.find_element(By.CSS_SELECTOR, 'div.quiz-component > textarea').send_keys(answer)
    # находим и нажимаем на кнопку "Отправить"
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    # ожидаем фидбека, проверяем корректность ответа
    hint = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    assert hint.text == "Correct!", "Feedback message are not 'Correct!'"



