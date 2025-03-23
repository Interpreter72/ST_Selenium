from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(7)
    browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# try:
#     link = "http://suninjuly.github.io/selects2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     num1 = browser.find_element(By.ID, "num1").text
#     num2 = browser.find_element(By.ID, "num2").text
#     sum = str(int(num1) + int(num2))

#     select = Select(browser.find_element(By.ID, "dropdown"))
#     select.select_by_value(sum)

#     browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()



#     # treasure_x = browser.find_element(By.ID, "treasure").get_attribute("valuex")

#     # browser.find_element(By.ID, "answer").send_keys(calc(treasure_x))

#     # browser.find_element(By.ID, "robotCheckbox").click()

#     # browser.find_element(By.ID, "robotsRule").click()

#     # browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

#     # time.sleep(1)

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(7)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
