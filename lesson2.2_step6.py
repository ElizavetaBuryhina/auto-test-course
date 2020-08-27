# Задание:
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

import math,time
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(answer)

button = browser.find_element_by_class_name('btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)



check_box = browser.find_element_by_id("robotCheckbox")
check_box.click()
radio = browser.find_element_by_id("robotsRule")
radio.click()


button.click()

time.sleep(10)
browser.quit()