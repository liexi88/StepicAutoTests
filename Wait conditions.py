from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)
browser = webdriver.Chrome(options=options)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id('book')

# говорим Selenium проверять в течение 14 секунд, пока текст не достигнет нужного значения
text = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
   ) 
button.click()

valuexId = browser.find_element_by_id("input_value")
valuex = valuexId.text

y = calc(valuex)

input2 = browser.find_element_by_id("answer")
input2.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()
