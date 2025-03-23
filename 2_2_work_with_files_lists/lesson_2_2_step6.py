from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value").text

    browser.find_element(By.ID, "answer").send_keys(calc(x_element))

    check_box = browser.find_element(By.ID, "robotCheckbox")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()

    radio_robot = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
    radio_robot.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # time.sleep(1)
    button.click()

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x_element))


    # time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
