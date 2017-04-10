import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time

locality = "Azzizyah!"
title_text = "Title Text"
mobile = "056111111"
description = "description"
e_address = "email@address.com"



def start_uploading():
    #launch selenium
    print("Preparing to uploading your Advertisement")
    web_driver_load()
    #open page
    driver.get("https://www.expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=223&category_title=Transportation")
    #write the locality
    print("Loading... Expatriates.com")
    time.sleep(1)
    location_ = driver.find_element_by_xpath('//*[@id="postAnAdStep2"]/input[1]')
    location_.send_keys(locality)
    print("Filling in the form!...")
    time.sleep(1)
    #click next
    location_.send_keys(Keys.RETURN)
    #wait for page to open
    write_details = driver.find_element_by_xpath('//*[@id="title"]')
    #write the title
    write_details.send_keys(title_text)
    time.sleep(1)
    num = driver.find_element_by_xpath('//*[@id="contact_number"]')
    #write the phone number
    num.send_keys(mobile)
    time.sleep(1)
    desc = driver.find_element_by_xpath('//*[@id="description"]')
    #Write the description
    desc.send_keys(description)
    time.sleep(1)
    ea = driver.find_element_by_xpath('//*[@id="email"]')
    #write the email address
    ea.send_keys(e_address)
    time.sleep(1)
    rad_btn = driver.find_element_by_xpath('//*[@id="postAnAd"]/ul/li[2]/input')
    rad_btn.click()
    time.sleep(1)
    #click next
    next_2 = driver.find_element_by_xpath('//*[@id="submit"]')
    print("Wrote your details!...")
    next_2.click()
    
    #wait for page to load
    #final_step = driver.find_element_by_xpath('//*[@id="title"]')
    #click print add
    #final_step = driver.find_element_by_xpath('//*[@id="submit"]')
    #print("Uploading your Advert...")
    #final_step.click()
    
    #your advertisement is not Posted
    print("Writing the history file, transportation-list.txt")
    write_file()
    quit_program('done')
    driver.close()
	#else:
    #   quit_program("all done")

def write_file():
    file = open('transportation-list.txt', 'a')
    file.write(material)
    
def web_driver_load():
    global driver
    print("Launching Chrome")
    driver = webdriver.Chrome()
    print("Chrome Launched!")
    #time.sleep(1)

def quit_program(data):
    if "not time" in data:
        print("Quiting program, today in not the Day!")
    elif "all done" in data:
        print("Your Advertisement was posted Today!!.")
    elif "done" in data:
        print("Your Advertisement is Now posted!.")
    quit()

if __name__ == "__main__":
    now = datetime.datetime.now()
    today = (str(now.day) + "." + str(now.month))
    material = "Ad Last Updated on : "+ str(now.strftime("%d-%B-%Y %I:%M.%S %p")) + "\n"
    login_exp()
    start_uploading()
