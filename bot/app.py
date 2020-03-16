import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bot import Bot

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('./Windscribe-Free-VPN-and-Ad-Blocker-Уеб-магазин-на-Chrome_v2.4.1.crx')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# PROXY = " 125.26.108.170:61637"
# chrome_options.add_argument(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(options=chrome_options)

print('')
print('########################')
print('If automation of mouse fails, possibly due to different screen size, check mouseclass and change mouse positions accordingly using mouseNow.py to determine position.')
print('########################')
print('Please log into vpn chrome extension.')
username, password = '', ''
print(f'username: {username}, password: {password}')
done = False
while not done:
    print('Ensure you close 1st and 3rd tab before proceeding.')
    ans = input('Enter y when done: ')
    if ans == 'y':
        done = True
    else:
        print('okay, waiting...')

stop = False
if done:
    bot = Bot(driver)
    print('created bot')
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
    if not stop:
        print('Registration for twitch with facebook successful!')
        print('waiting for twitch verification email to be sent')
        bot.confirm_twitch()

        print('storing verified bot info')
        bot.store_info()

        print('bot succesfully created. do you want to interact with any channels? ')
        interact = input('y/n? :')

        if interact == 'y':
            channel_list = input('input channels to follow, separated by a whitespace: ').strip().split()
            print('following channels now')
            bot.interact_channels(channel_list)


print('end of test')
print('Close browser?')
fin = input('y/n: ')
if fin == 'y':
    bot.driver.quit()
else:
    pass
