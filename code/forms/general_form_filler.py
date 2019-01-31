from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
import os

# This script works fine!
email_address = 'salikhundmiri@gmail.com'
password = 'yxwedVLPLxBJa7r'

def notify(title, text, subtitle):
    if subtitle:
        os.system("""
        osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Hero"'
        """.format(title, subtitle, text))
    else:
        os.system("""
        osascript -e 'display notification "{}" with title "{}" sound name "Hero"'
        """.format(title, text))

def launch_chrome(title_text):
    global driver
    print_text_1 = "Attempting to post " + str(title_text)
    print("Launching Chrome")
    # notify("Launching Chrome...", "Posting on expatriates.com", None)
    notify(print_text_1, "Posting on expatriates.com", None)

    driver = webdriver.Chrome('/Library/SeleniumWebDrivers/WebDrivers/chromedriver')
    print("Chrome Launched!")
    time.sleep(1)

def open_website(page_link, locality, title_text, mobile, description, e_address, PUBLISH):
    #open page
    driver.get(page_link)

    print_text_1 = "Attempting to post " + str(title_text)
    # send notification to user.
    # notify(print_text_1, "Posting on expatriates.com", None)

    print(print_text_1)
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
        
    print(driver.title)

    if driver.title == 'expatriates.com - Thank you!':
        return True
    else:
        return False

    # if assert is true, then return True. Else return False.

def post_advert(page_link, locality, title_text, mobile, description, e_address, PUBLISH):

    if PUBLISH:
        launch_chrome(title_text)
    else:
        notify(title_text, "Post on expatriates.com", "!!ALERT!!")

    if open_website(page_link, locality, title_text, mobile, description, e_address, PUBLISH):
        notify_text = "Ad: " + title_text
        print("Form completed!")
        notify( notify_text,'Please check your email address.', "Advert Posted!")

    else:
        notify_text = "Ad: " + title_text
        print("Form Submission failed.")
        notify( notify_text,'Please run the script again.', "Advert Failed!")

    driver.close()

if __name__ == '__main__':
    post_advert()