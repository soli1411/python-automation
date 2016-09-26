#Sends automatically messages to one of yours whatsapp contacts

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	chromedriver="/Users/Lorenzo/Downloads/chromedriver"
	os.environ["webdriver.chrome.driver"]=chromedriver
	driver=webdriver.Chrome(chromedriver)
        
## quit web driver for selenium
def web_driver_quit():
	driver.quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	wait(10)#waits 10 seconds so you can scan qr and log in and select a chat
	print("login shuold have been done already!")
        
def sendMessage(msg):
	web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)


### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	wait()
	#sending 50 messages
	for i in range(50):
		sendMessage("Tin!")
	print("Process complete successfully")

	wait()
	web_driver_quit()
