from selenium import webdriver
import time
import math
import os
  
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("email@yandex.ru")
 
# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, 'empty.txt')        

element = browser.find_element_by_id("file")
element.send_keys(file_path)

button = browser.find_element_by_tag_name("button")

button.click()
