from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client

#TWILIO ACCOUNT
account_sid = ''
auth_token = ''

#BAND ACCOUNT
EMAIL_USER = ''
PASSWORD_USER = ''


client = Client(account_sid, auth_token)

#PhoneNumbers
TWILIO_NUM = ' '
MY_NUM = ' '


driver = webdriver.Chrome()

driver.get(
    "https://auth.band.us/login_page?next_url=https%3A%2F%2Fband.us%2Fhome%3Freferrer%3Dhttps%253A%252F%252Fband.us%252Fen%252Fsign_in")

driver.maximize_window()  # For maximizing window
driver.implicitly_wait(20)

search_box = driver.find_element(By.ID, "email_login_a")

search_box.send_keys("Selenium" + Keys.ENTER)

emailBox = driver.find_element(By.NAME, "email")

driver.implicitly_wait(20)

emailBox.send_keys(EMAIL_USER + Keys.ENTER)

passwordBox = driver.find_element(By.NAME, "password")
driver.implicitly_wait(20)

passwordBox.send_keys(PASSWORD_USER + Keys.ENTER)

driver.implicitly_wait(50)
cookiesButton = driver.find_element(By.CLASS_NAME, "bcm_btnCookieOn")
cookiesButton.click()

#################Second STEP CHAT ########################

driver.get('https://band.us/band/85715297/chat/CcC7c7')
driver.implicitly_wait(50)

cover = False

msgCount = 20


textbox = driver.find_element(By.ID, 'write_comment_view88')
while not cover:
    time.sleep(5)
    if driver.find_elements_by_xpath(
            '//*[@id="wrap"]/div[1]/div[2]/div[2]/div/div/div[2]/div[{}]/div/div[1]/div[1]/span'.format(msgCount)):
        time.sleep(3)
        link = driver.find_elements_by_xpath(
            '//*[@id="wrap"]/div[1]/div[2]/div[2]/div/div/div[2]/div[{}]/div/div[1]/div[1]/span'.format(msgCount))

        b = ""
        for i in link:
            print(i.text)
            b = i.text
            if ("swap" in b) or ("switch" in b):
                print("not a shift")
            elif ("thursday" in b and "10" in b and "2" in b) or ("monday" in b and "2" in b and "6" in b) or (
                    "wednesday" in b and "2" in b and "6" in b) or ("friday" in b and "10" in b and "2" in b):
                print("already have that shift")
            elif (("today" in b) or ("tonight" in b) or ("tomorrow" in b)) and (
                    ("close" in b) or ("closing" in b) or ("cover" in b)):
                print("shift1")
                message = client.messages.create(
                    from_='+12512374403',
                    body='shift open, check the band app',
                    to='+15597362064'
                )
                textbox.send_keys("I can cover")
            elif (("1" in b) or ("2" in b) or ("3" in b) or ("4" in b) or ("5" in b) or ("6" in b) or ("7" in b) or (
                    "8" in b) or ("9" in b)) and (
                    ("cover" in b) or ("today" in b) or ("tonight" in b) or ("tomorrow" in b)):
                print("shift2")
                message = client.messages.create(
                    from_=TWILIO_NUM,
                    body='shift open, check the band app',
                    to=MY_NUM
                )
                textbox.send_keys("I can cover" )
            else:
                print("Just a regular message")
            msgCount = msgCount + 1
    else:
        #print("NO MESSAGE FOUND<><><><><><>TRYING AGAIN")
        driver.implicitly_wait(30)
