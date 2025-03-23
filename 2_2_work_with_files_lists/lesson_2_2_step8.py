
from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Milos")
    browser.find_element(By.NAME, "lastname").send_keys("Vucic")
    browser.find_element(By.NAME, "email").send_keys("milos.vucic@ya.rs")

    # with open("file.txt", "w") as file:
    #     content = file.write("test")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
