from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time

# This script works fine!

def launch_chrome():
    global driver
    print("Launching Chrome")
    driver = webdriver.Chrome('/Library/SeleniumWebDrivers/WebDrivers/chromedriver')
    print("Chrome Launched!")
    time.sleep(1)

def open_website(page_link, locality, title_text, mobile, description, e_address, PUBLISH):
    #open page
    driver.get(page_link)
    print("Attempting to post '" + str(title_text) + "' on expatriates.com")
    assert "expatriates.com - Place a Free Ad Step 2 of 3" in driver.title

    print("Page loaded Successfully!")
    print("Filling in the form!...")

    location_ = driver.find_element_by_xpath('//*[@id="postAnAdStep2"]/input[1]')
    location_.send_keys(locality)
    time.sleep(1)
    print("Wrote Locality.")
    #click next
    location_.send_keys(Keys.RETURN)
    #wait for page to open
    write_details = driver.find_element_by_xpath('//*[@id="title"]')
    #write the title
    write_details.send_keys(title_text)
    time.sleep(1)
    print("Wrote Title text.")
    
    if mobile:
        num = driver.find_element_by_xpath('//*[@id="contact_number"]')
        # write the phone number
        num.send_keys(mobile)
        print("Wrote Mobile Number.")
        time.sleep(1)
    
    desc = driver.find_element_by_xpath('//*[@id="description"]')
    #Write the description
    desc.send_keys(description)
    time.sleep(1)
    print("Wrote Description.")

    ea = driver.find_element_by_xpath('//*[@id="email"]')
    #write the email address
    ea.send_keys(e_address)
    time.sleep(1)
    print("Wrote email Address.")

    rad_btn = driver.find_element_by_xpath('//*[@id="postAnAd"]/ul/li[2]/input')
    rad_btn.click()
    time.sleep(1)

    if PUBLISH:
        print("Publishing...")
        ea.send_keys(Keys.RETURN)
        time.sleep(5)
    assert "expatriates.com" in driver.title
    print("Form completed!")

def post_advert(page_link, locality, title_text, mobile, description, e_address, PUBLISH):
    # print(page_link)
    # print(locality)
    # print(title_text)
    # print(mobile)
    # print(description)
    # print(e_address)
    # print(PUBLISH)
    launch_chrome()
    open_website(page_link, locality, title_text, mobile, description, e_address, PUBLISH)
    driver.close()

if __name__ == '__main__':
    post_advert()