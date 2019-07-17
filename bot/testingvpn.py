from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_extension('./Windscribe-Free-VPN-and-Ad-Blocker-Уеб-магазин-на-Chrome_v2.4.1.crx')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://windscribe.com/login')
username, password = 'theweekencl', 'Cn57hksWy8xMTAe'
time.sleep(5)
username_box = driver.find_element_by_id('username')
username_box.send_keys(username)
time.sleep(1)
password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
time.sleep(1)
login_button = driver.find_element_by_id('login_button')
login_button.click()

