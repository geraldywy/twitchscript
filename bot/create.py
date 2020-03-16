import time
import random
from gen import gen_userpass, gen_name
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bot import Bot
from mouseclass import Mouse

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('./Windscribe-Free-VPN-and-Ad-Blocker-Уеб-магазин-на-Chrome_v2.4.1.crx')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# PROXY = " 125.26.108.170:61637"
# chrome_options.add_argument(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(options=chrome_options)

print('')
n = int(input('Attempt to create how many bots? '))
print('Logging into vpn chrome extension. Do not touch the mouse or driver.')
username, password = '', ''
print(f'username: {username}, password: **hidden**')
mouse = Mouse()
mouse.log_in_vpn()
print('logged into vpn extension, you may now move the driver and mouse.')

stop = False
for i in range(1, n+1):
    bot = Bot(driver)
    print(f'creating bot number {i}')
    bot.open_chrome()
    print('getting email')
    bot.get_email()
    print(bot)
    print('bot signing up for facebook')
    bot.sign_up_facebook()
    print('sign up for facebook done!')
    print('checking email to verify facebook')
    bot.confirm_facebook()
    print('bot signing up for twitch')
    try:
        bot.sign_up_twitch_with_facebook()
    except:
        print('detected by facebook, stopping script. Try again later.')
        stop = True
    if stop:
        print(f'{i-1} bots created successfully.')
        break
    else:
        print('Registration for twitch with facebook successful!')
        print('waiting for twitch verification email to be sent')
        bot.confirm_twitch()

        print('storing verified bot info')
        bot.store_info()
        if i != n:
            print('clearing session for next bot')
            bot.twitch_logout()
            print('twitch logged out')
            bot.facebook_logout()
            print('facebook logged out')
            bot.open_chrome()
            print('waiting for next new email, 10 mins to be safe.')
            time.sleep(60*10) #wait for full 10 mins to be safe
    if i == n:
        print(f'All {n} bots created successfully. Closing driver.')

driver.quit()
