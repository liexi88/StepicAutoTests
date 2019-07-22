from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
button.click()


new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

valuexId = browser.find_element_by_id("input_value")
valuex = valuexId.text

y = calc(valuex)

input2 = browser.find_element_by_id("answer")
input2.send_keys(y)

button = browser.find_element_by_tag_name("button")
button.click()
