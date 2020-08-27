# Задание:
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

import math,time
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(answer)
check_elements = browser.find_elements_by_class_name('form-check-label')
for check_element in check_elements:
    check_element.click()

button = browser.find_element_by_class_name('btn')
button.click()

time.sleep(10)
browser.quit()

