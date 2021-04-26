from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    num1 = int(x)
    num2 = int(y)

    z = str(num1 + num2)
    

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z) # ищем элемент

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

  

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()