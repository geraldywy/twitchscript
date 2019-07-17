import time
import random
from gen import gen_userpass, gen_name
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from gen import gen_userpass, gen_name

class Bot:

    def __init__(self, driver):
        self.name = gen_name()
        self.username = gen_userpass()
        self.password = gen_userpass()[:12][::-1]
        self.email = None
        self.birthday = (random.randint(1, 28), random.randint(1, 12), random.randint(1939, 2005))
        self.sex = random.choice([1, 2])
        sex_dict = {1: 'Female', 2:'Male'}
        self.sex_literal = sex_dict[self.sex]
        self.driver = driver
    
    def open_chrome(self):
        driver = self.driver
        driver.get('https://www.google.com')
        time.sleep(3)
    
    def sign_up_twitch_with_facebook(self):
        driver = self.driver
        driver.get('https://www.twitch.tv/')
        time.sleep(2) # Let the user actually see something!
        signup_button = driver.find_element_by_xpath('//button[@data-a-target="signup-button"]')
        signup_button.click()
        time.sleep(5) # let sign up form load
        connect_with_fb = driver.find_element_by_xpath('//button[@class="facebook-connect-button"]')
        connect_with_fb.click()
        time.sleep(5)
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        signin_window_handle = None
        while not signin_window_handle:
            for handle in driver.window_handles:
                if handle != main_window_handle:
                    signin_window_handle = handle
                    break
        driver.switch_to.window(signin_window_handle)
        continue_as_bot = driver.find_element_by_xpath('//button[@name="__CONFIRM__"]')
        continue_as_bot.click()
        time.sleep(5)
        driver.switch_to.window(main_window_handle)
        # no unique identifiers for username box, but when clicking signup, it auto selects usernamebox, so just input username
        try:
            username_box = driver.find_element_by_xpath('(//input[@data-a-target="tw-input"])[2]')
            username_box.clear()
            username_box.send_keys(self.username) 
        except:
            actions = ActionChains(driver)
            actions.send_keys(self.username)
            actions.perform()
        time.sleep(1)
        password_box = driver.find_element_by_xpath('//input[@autocomplete="current-password"]')
        password_box.clear()
        password_box.send_keys(self.password)
        time.sleep(1)
        password_box.send_keys(Keys.RETURN)
        time.sleep(20)


    def __repr__(self):
        return f"Bot's name: {self.name}\nBot's username: {self.username}\nBot's password: {self.password}\nBot's Sex: {self.sex_literal}\nBot's birthday: {self.birthday}\nBot's Email: {self.email}"

    def get_email(self):
        driver = self.driver
        driver.get('https://10minutemail.com/10MinuteMail/index.html')
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        email_field = driver.find_element_by_xpath("//input[@class='mail-address-address']")
        email = email_field.get_attribute('value')
        self.email = email
    
    def sign_up_facebook(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        time.sleep(5)
        firstname_box = driver.find_element_by_xpath("//input[@name='firstname']")
        firstname_box.send_keys(self.name[0])
        lastname_box = driver.find_element_by_xpath("//input[@name='lastname']")
        lastname_box.send_keys(self.name[1])
        email_box = driver.find_element_by_xpath("//input[@name='reg_email__']")
        email_box.send_keys(self.email)
        time.sleep(1)
        email_box_2 = driver.find_element_by_xpath("//input[@name='reg_email_confirmation__']")
        email_box_2.send_keys(self.email)
        password_box = driver.find_element_by_xpath("//input[@data-type='password']")
        password_box.send_keys(self.password)
        b_day = driver.find_element_by_xpath("//select[@name='birthday_day']")
        b_day.click()
        time.sleep(0.5)
        day = str(self.birthday[0])
        b_day = driver.find_element_by_xpath(f"//option[@value={day}]")
        b_day.click()
        time.sleep(0.5)
        b_month = driver.find_element_by_xpath("//select[@name='birthday_month']")
        b_month.click()
        time.sleep(0.5)
        month = str(self.birthday[1])
        b_month = driver.find_element_by_xpath(f"//select[@name='birthday_month']/option[@value={month}]")
        b_month.click()
        time.sleep(0.5)
        b_year = driver.find_element_by_xpath("//select[@name='birthday_year']")
        b_year.click()
        time.sleep(0.5)
        year = str(self.birthday[2])
        b_year = driver.find_element_by_xpath(f"//option[@value={year}]")
        b_year.click()
        time.sleep(0.5)
        sex = str(self.sex)
        sex = driver.find_element_by_xpath(f"//input[@name='sex'][@value={sex}]")
        sex.click()
        time.sleep(5)
        submit = driver.find_element_by_xpath("//button[@name='websubmit']")
        while True:
            try:
                submit.click()
                print('clicked submit')
            except:
                break
            finally:
                time.sleep(10)
        print('waiting for facebook email to be sent')
        time.sleep(20)

    def confirm_facebook(self):
        driver = self.driver
        driver.get('https://10minutemail.com/10MinuteMail/index.html')
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        found = False
        while not found:
            try:
                inc_mail = driver.find_element_by_xpath("//span[@class='inc-mail-subject']")
                found = True
            except:
                print('facebook email not found, waiting 10s')
                time.sleep(10)
        inc_mail.click()
        print('opening facebook email!')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        confirm_link = driver.find_element_by_link_text('Action required: Confirm your Facebook account')
        print('found link!')
        confirm_link.click()
        print('clicked link')
        time.sleep(10)

    def interact_channels(self, channels):
        driver = self.driver
        for channel in channels:
            try:
                driver.get(f'https://www.twitch.tv/{channel}')
                time.sleep(10)
                follow_button = driver.find_element_by_xpath("//button[@data-a-target='follow-button']")
                follow_button.click()
                print(f'followed {channel}')
                try:
                    time.sleep(10)
                    chatbox = driver.find_element_by_xpath("//textarea[@data-a-target='chat-input']")
                    chatbox.click()
                    try:
                        chatrules_ok = driver.find_element_by_xpath("//button[@data-test-selector='chat-rules-ok-button']")
                        chatrules_ok.click()
                    except:
                        print('no rules to click ok')
                    finally:
                        chatbox.click()
                        chatbox.send_keys('Hi. I am a bot :)')
                        chatbox.send_keys(Keys.RETURN)
                        time.sleep(5)
                        chatbox.send_keys('no Kappa')
                        chatbox.send_keys(Keys.RETURN)
                        time.sleep(15)
                except:
                    print(f'cant find chatbox for {channel}')
            except:
                print(f'failed to follow {channel}, invalid channel link.')
                time.sleep(5)    

    def confirm_twitch(self):
        driver = self.driver
        driver.get('https://10minutemail.com/10MinuteMail/index.html')
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        found = False
        while not found:
            try:
                inc_mail = driver.find_element_by_xpath("//*[text()='no-reply@twitch.tv']")
                found = True
            except:
                print('twitch email not found, waiting for 10s')
                time.sleep(10)
                driver.get('https://10minutemail.com/10MinuteMail/index.html')
                
        inc_mail.click()
        print('opening twitch email!')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        confirm_link = driver.find_element_by_link_text('Verify your account')
        print('found link!')
        confirm_link.click()
        print('clicked link')
        time.sleep(5)

    def store_info(self):
        with open('bot accounts', 'a') as f:
            f.write(f"{self.username}, {self.password}, {self.email}\n")
    
    def facebook_logout(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        time.sleep(5)
        found = False
        while not found:
            try:
                navigation_arrow = driver.find_element_by_id('userNavigationLabel')
                found = True
            except:
                print('couldnt find navigation arrow, refreshing facebook')
                driver.get('https://www.facebook.com/')
                time.sleep(5)
        navigation_arrow.click()
        time.sleep(1)
        log_out = False
        while not log_out:
            try:
                log_out_button = driver.find_element_by_xpath("(//span[@class='_54nh'])[6]")
                log_out_button.click()
                log_out = True
            except:
                print('log out button not found, attemping to find again')
                time.sleep(1)
        time.sleep(5)
        removed = False
        while not removed:
            try:
                remove_button = driver.find_element_by_xpath("(//a[@role='button'])[1]")
                removed = True
            except:
                print('remove profile button not found')
        remove_button.click()
        time.sleep(3)

    def twitch_logout(self):
        driver = self.driver
        found = False
        while not found:
            try:
                avatar = driver.find_element_by_xpath("(//img[@class='tw-avatar__img tw-block tw-border-radius-rounded tw-image'])[1]")
                found = True
            except:
                print('couldnt find avatar pic, refreshing twitch.')
                driver.get('https://www.twitch.tv/')
                time.sleep(5)
        avatar.click()
        time.sleep(2)
        log_out = driver.find_element_by_xpath("//*[text()='Log Out']")
        log_out.click()
        time.sleep(5)