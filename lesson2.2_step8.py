# Задание:
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"


from selenium import webdriver
import time,os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("email")

file_button = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir,'file.txt')
file_button.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)
browser.quit()
