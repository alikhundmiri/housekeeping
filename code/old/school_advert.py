from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time

# This script works fine! 

# CONTROL CENTER
PHONE_NUMBER = True
PUBLISH = True


locality = "Azzizyah - Near Chennai Darbar"
title_text = "Star Play Group - Best Kindergarten for your kids"
mobile = "0565179202"
description = '''
The Best Kindergarten for your kids has moved to a *new* location! 

We are accepting new students now! 

* Lots of toys and props for kids to play with. 
* Taught by Affectionate Indian teachers, 
* Suitable Furniture for the kids, 
* Study Material is provided. 
* Overhead projector, 

Curiosity starts here. 
Nurturing starts here. 
Learning starts, here. 

Official Star Play Group website: https://goo.gl/iW6LLj 

Location: 
Behind Chennai Darbar. 
Near to Sameera polyclinic. Al Aziziyah. 

Visiting hours to be followed STRICTLY: 
1:00 PM - 4:00 PM 

Call to book an appointment: 056 517 9202

'''
e_address = "salikhundmiri@gmail.com"



def launch_chrome():
    global driver
    print("Launching Chrome")
    driver = webdriver.Chrome('/Library/SeleniumWebDrivers/WebDrivers/chromedriver')
    print("Chrome Launched!")
    time.sleep(1)

def open_website():
    #open page
    driver.get("http://expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=158&category_title=Nursery%20Schools")
    print("Loading... Expatriates.com")
    assert "expatriates.com - Place a Free Ad Step 2 of 3" in driver.title


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
    
    if PHONE_NUMBER:
        num = driver.find_element_by_xpath('//*[@id="contact_number"]')
        # write the phone number
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

    if PUBLISH:
        ea.send_keys(Keys.RETURN)
        time.sleep(5)
    assert "expatriates.com" in driver.title
 

if __name__ == '__main__':
    launch_chrome()
    open_website()
    driver.close()
