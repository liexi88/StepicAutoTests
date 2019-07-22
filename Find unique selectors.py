from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Код, который заполняет обязательные поля

input1 = browser.find_element_by_css_selector("div.first_block .first")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("div.first_block .second")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("div.first_block .third")
input3.send_keys("email@yandex.ru")
input4 = browser.find_element_by_css_selector("div.second_block .first")
input4.send_keys("74955555555")
input5 = browser.find_element_by_css_selector("div.second_block .second")
input5.send_keys("Smolensk")

time.sleep(2)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")

# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

