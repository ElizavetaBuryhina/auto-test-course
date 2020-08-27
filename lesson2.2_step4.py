import math,time
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)
treasure_box = browser.find_element_by_id('treasure')
x = treasure_box.get_attribute('valuex')
answer = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(answer)
check_box = browser.find_element_by_id("robotCheckbox")
check_box.click()
radio = browser.find_element_by_id("robotsRule")
radio.click()

button = browser.find_element_by_class_name('btn')
button.click()

time.sleep(10)
browser.quit()