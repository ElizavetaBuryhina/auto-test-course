# Задание:
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

import time, math
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/explicit_wait2.html"


browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_id('book')
WebDriverWait(browser,12).until(
    EC.text_to_be_present_in_element((By.ID,'price'),'100'))
button.click()

button = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView(true)",button)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(answer)

button.click()


time.sleep(10)
browser.quit()