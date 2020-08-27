# Задание:
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

import time, math
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"


browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_class_name('btn')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(answer)

button = browser.find_element_by_class_name('btn')
button.click()


time.sleep(10)
browser.quit()