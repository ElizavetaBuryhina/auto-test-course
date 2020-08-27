# Задание:
# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1_el = browser.find_element_by_id('num1')
num1 = num1_el.text
num2_el = browser.find_element_by_id('num2')
num2 = num2_el.text
sum_num = str(int(num1) + int(num2))
print(sum_num)
select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(sum_num)

button = browser.find_element_by_class_name('btn')
button.click()

time.sleep(10)
browser.quit()