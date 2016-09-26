#Sends automatically messages to your friends on facebook using python and selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

#wait for browser to open
def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	chromedriver="/Users/Soli/Downloads/chromedriver"#path to chromedriver.exe
	os.environ["webdriver.chrome.driver"]=chromedriver
	driver=webdriver.Chrome(chromedriver)
	driver.maximize_window()
        
## quit web driver - selenium
def web_driver_quit():
	driver.quit()

## login in app site
def facebook_login():
	driver.get('https://facebook.com/');
	wait()
	web_obj = driver.find_element_by_name('email')
	web_obj.send_keys(input())#email
	web_obj = driver.find_element_by_name('pass')
	web_obj.send_keys(input())#password
	web_obj.send_keys(Keys.RETURN)
	wait()

def sendMessage(friend_name,msg,times,delay):
        driver.get('https://www.facebook.com/messages/'+friend_name)
        wait()
        web_obj=driver.find_element_by_class_name('uiTextareaNoResize')
        for i in range(0,times):
            web_obj.send_keys(msg+Keys.RETURN)
            wait(delay)

### Main Method
if __name__ == "__main__":
	web_driver_load()
	facebook_login()
	sendMessage('george.lucas','Tin!',100,0)
	web_driver_quit()
