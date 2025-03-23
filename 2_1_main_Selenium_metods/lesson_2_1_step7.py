from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_x = browser.find_element(By.ID, "treasure").get_attribute("valuex")

    browser.find_element(By.ID, "answer").send_keys(calc(treasure_x))

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    # time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
