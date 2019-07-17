from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# PROXY = " 125.26.108.170:61637"
# chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.twitch.tv/')
time.sleep(2) # Let the user actually see something!
login_button = driver.find_element_by_xpath('//button[@data-a-target="login-button"]')
login_button.click()
time.sleep(5) # let sign up form load
username_box = driver.find_element_by_xpath('(//input[@data-a-target="tw-input"])[2]')
username_box.clear()
username_box.send_keys('blitzattune835')
time.sleep(1)
password_box = driver.find_element_by_xpath('//input[@autocomplete="current-password"]')
password_box.clear()
password_box.send_keys('uohlisrepuap')
time.sleep(1)
password_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.get('https://www.twitch.tv/noah_almont')
try:
    follow_button = driver.find_element_by_xpath("//button[@data-a-target='follow-button']")
    follow_button.click()
    print(f'followed {channel}')
except:
    print('already followed')
try:
    time.sleep(10)
    chatbox = driver.find_element_by_xpath("//textarea[@data-a-target='chat-input']")
    chatbox.click()
    try:
        chatrules_ok = driver.find_element_by_xpath("//button[@data-test-selector='chat-rules-ok-button']")
        chatrules_ok.click()
    except:
        print('no rules to click ok')
    chatbox.click()
    chatbox.send_keys('Hi. I am a bot :)')
    chatbox.send_keys(Keys.RETURN)
    time.sleep(5)
    chatbox.send_keys('no Kappa')
    chatbox.send_keys(Keys.RETURN)
    time.sleep(5)
except:
    print('cant find chat box')

print('all done!')