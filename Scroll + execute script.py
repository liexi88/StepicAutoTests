from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()

link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

valuexId = browser.find_element_by_id("input_value")
valuex = valuexId.text

y = calc(valuex)

button = browser.find_element_by_tag_name("button")
# script with scroll to hidden button
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

input2 = browser.find_element_by_id("answer")
input2.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option1 = browser.find_element_by_id("robotsRule")
option1.click()

button.click()
assert True
