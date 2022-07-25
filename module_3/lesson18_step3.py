# открыть страницу 
# ввести правильный ответ 
# нажать кнопку "Отправить" 
# дождаться фидбека о том, что ответ правильный 
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, 'div.quiz-component > textarea').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    # hint = WebDriverWait(browser, 12).until(
    #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.smart-hints__hint"), 'Correct!')
    # )
    hint = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    assert hint.text == "Correct!", "Feedback message are not 'Correct!'"



