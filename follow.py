from bot import Bot
import time
import random
from gen import gen_userpass, gen_name
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bot import Bot
from mouseclass import Mouse


with open('C:/Users/Gerald/Desktop/bot/bot accounts', 'r') as f:
    next(f) #skip header
    content = f.readlines()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('C:/Users/Gerald/Desktop/bot/Windscribe-Free-VPN-and-Ad-Blocker-Уеб-магазин-на-Chrome_v2.4.1.crx')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# PROXY = " 125.26.108.170:61637"
# chrome_options.add_argument(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(options=chrome_options)

print()
channel_list = input("Follow which channel(s)? Split them with 1 whitespace: ").strip().split()
print()
f = input('Chat? y/n: ')
if f.lower() == 'y':
    f = True
else:
    f = False
print()
print('Logging into vpn chrome extension. Do not touch the mouse or driver.')
username, password = 'theweekencl', 'Cn57hksWy8xMTAe'
print(f'username: {username}, password: **hidden**')
mouse = Mouse()
mouse.log_in_vpn()
print('logged into vpn extension, you may now move the driver and mouse.')

i = 1
driver.get('https://www.google.com/') # work around vpn messing with driver.
time.sleep(5)
driver.get('https://www.google.com/')
time.sleep(5)
for line in content:
    print(f'bot number {i} following channel')
    
    clean = line.split(', ')
    username, password, email = clean[0], clean[1], clean[2]
    bot = Bot(driver, username, password, email)
    # log into twitch
    try:
        bot.interact_channels(channel_list, logged_in=False, chat=f)
        print(f'successful for bot {i}')
    except Exception as error:
        print('Caught this error: ' + repr(error))
        print(f'Failed to login, check\nusername:{bot.username}, password:{bot.username}')
    try:
        bot.twitch_logout()
        print("logged out twitch")
    except:
        pass
    i += 1

print('all done !')

