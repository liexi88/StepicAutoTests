from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Поиск значения через атрибут для вычисления формулы
valuexId = browser.find_element_by_id("treasure")
valuex = valuexId.get_attribute("valuex")

y = calc(valuex)

# Отправка решения
input2 = browser.find_element_by_id("answer")
input2.send_keys(y)

# Заполнение Чекбоксов и Радио
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option1 = browser.find_element_by_id("robotsRule")
option1.click()

time.sleep(2)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)


