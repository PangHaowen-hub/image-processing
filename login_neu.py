from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get("https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1")
time.sleep(8)

username_input = driver.find_element_by_id("un")
password_input = driver.find_element_by_id("pd")
print('Searching connect')
login_button = driver.find_element_by_id("index_login_btn")
print('Find connect successfully')
username_input.send_keys('2071231')  # username_input为登录账号
password_input.send_keys('phw15963')  # password_input为登录密码
time.sleep(10)
print('Input user info')
login_button.click()
print('Connect')

time.sleep(3)
driver.close()
