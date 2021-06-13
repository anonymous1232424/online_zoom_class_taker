# Importing the necessary packages .

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from info import *
import keyboard
import schedule
import discord_webhook

CURRENT_DAY = datetime.datetime.now().strftime("%a")

# Adding options .

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

# Creating a Driver object .
# Download the driver according to your version from here https://chromedriver.chromium.org/downloads .
driver = webdriver.Chrome("YOUR DRIVER PATH", options=opt)


# Login Function
def login_to_zoom(email, password):
    global driver
    driver.get("https://zoom.us/signin")  # Zoom's Login page .
    time.sleep(3)
    driver.find_element_by_link_text("Google").click()  # Login from google option
    time.sleep(2)
    email_field = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div["
        "1]/div/div[1]/div/div[1]/input "
    )
    email_field.click()
    email_field.send_keys(email)  # Sending email key strokes !
    time.sleep(.5)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
    time.sleep(2)
    pass_field = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div["
        "1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    pass_field.click()
    pass_field.send_keys(password)  # Sending Password !
    time.sleep(.5)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
    time.sleep(4)


login_to_zoom("YOUR EMAIL", "YOUR PASSWORD")  # Provide your gmail and password here .


# Main Join Function .
def join_with_id_pass(class_name, id, password):
    driver.get("https://us05web.zoom.us/join")
    time.sleep(4)

    id_field = driver.find_element_by_id("join-confno")
    id_field.click()
    id_field.send_keys(id)  # Sending class id .
    time.sleep(.5)

    driver.find_element_by_link_text("Join").click()
    time.sleep(4)

    # 1st popup
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(1)

    # Launch meeting btn
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div").click()
    time.sleep(1)

    # 2nd popup
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(1)

    # Joining from browser
    driver.find_element_by_link_text("Join from Your Browser").click()
    time.sleep(4)

    # Turning of Mic and Video
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div[3]/div[3]/div[2]/div/div[3]/div[1]/button[1]/div").click()
    time.sleep(.5)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[3]/div[2]/div/div[3]/div[2]/button/div").click()

    # Join btn
    driver.find_element_by_id("joinBtn").click()
    time.sleep(4)

    passwd_field = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[3]/form/div/div[2]/div[1]/input")
    passwd_field.click()
    passwd_field.send_keys(password)  # Sending class password .
    time.sleep(1)
    # Join btn
    driver.find_element_by_id("joinBtn").click()
    join_time = datetime.datetime.now()

    # Sending the Message to us via Discord-Webhook
    discord_webhook.send_message(class_name=class_name, status="Joined", joined_time=join_time.strftime("%H:%M"),
                                 end_time=((join_time + datetime.timedelta(minutes=40)).strftime("%H:%M")))

    # Sleeping the program for the class running time.
    time.sleep(2400)
    left_time = datetime.datetime.now().strftime("%H:%M")
    driver.quit()

    # Sending the Left Message to us via Discord-Webhook
    discord_webhook.send_message(class_name=class_name, status="Left", joined_time=join_time, end_time=left_time)


# Scheduler here , Modify it according to your timetable .
# You may have less or more classes just modify the scheduler .
# Pass the name, ID, Password for the meeting in the same order .
# At 0 index we have our meeting ID, 1 index we have password, and the 2'nd index is the name of the class.

# Note there is no timetable for Tuesday and Saturday , But you can add them also .
def schedule_monday_class():
    schedule.every().monday.at(firstClass).do(join_with_id_pass, maths[2], maths[0], maths[1])
    schedule.every().monday.at(secondClass).do(join_with_id_pass, english[2], english[0], english[1])
    # schedule.every().monday.at(thirdClass).do(join_with_id_pass)
    schedule.every().monday.at(fourthClass).do(join_with_id_pass, geography[2], geography[0], geography[1])
    schedule.every().monday.at(fifthClass).do(join_with_id_pass, hindi[2], hindi[0], hindi[1])
    schedule.every().monday.at(sixthclass).do(join_with_id_pass, economics[2], economics[0], economics[1])
    while True:
        schedule.run_pending()
        time.sleep(1)


def schedule_wednesday_class():
    schedule.every().wednesday.at(firstClass).do(join_with_id_pass, maths[2], maths[0], maths[1])
    schedule.every().wednesday.at(secondClass).do(join_with_id_pass, english[2], english[0], english[1])
    schedule.every().monday.at(thirdClass).do(join_with_id_pass, biology[2], biology[0], biology[1])
    schedule.every().wednesday.at(fourthClass).do(join_with_id_pass, history[2], history[0], history[1])
    # schedule.every().wednesday.at(fifthClass).do(join_with_id_pass, hii[0], hin[1])
    schedule.every().wednesday.at(sixthclass).do(join_with_id_pass, hindi[2], hindi[0], hindi[1])

    # Here we are Constantly checking for any pending loops !
    while True:
        schedule.run_pending()
        time.sleep(1)


def schedule_thursday_class():
    schedule.every().thursday.at(firstClass).do(join_with_id_pass, maths[2], maths[0], maths[1])
    schedule.every().thursday.at(secondClass).do(join_with_id_pass, english[2], english[0], english[1])
    # schedule.every().monday.at(thirdClass).do(join_with_id_pass, )
    schedule.every().thursday.at(fourthClass).do(join_with_id_pass, history[2], history[0], history[1])
    schedule.every().thursday.at(fifthClass).do(join_with_id_pass, biology[2], biology[0], biology[1])
    schedule.every().thursday.at(sixthclass).do(join_with_id_pass, hindi[2], hindi[0], hindi[1])
    while True:
        schedule.run_pending()
        time.sleep(1)


def schedule_friday_class():
    schedule.every().friday.at(firstClass).do(join_with_id_pass, computer[2], computer[0], computer[1])
    schedule.every().friday.at(secondClass).do(join_with_id_pass, physics[2], physics[0], physics[1])
    schedule.every().monday.at(thirdClass).do(join_with_id_pass, english[2], english[0], english[1])
    schedule.every().thursday.at(fourthClass).do(join_with_id_pass, history[2], history[0], history[1])
    schedule.every().thursday.at(firstClass).do(join_with_id_pass, maths[2], maths[0], maths[1])
    schedule.every().thursday.at(fifthClass).do(join_with_id_pass, biology[2], biology[0], biology[1])
    while True:
        schedule.run_pending()
        time.sleep(1)


# According to the day We are setting the scheduler !

if CURRENT_DAY == "Mon":
    schedule_monday_class()

elif CURRENT_DAY == "Tue":
    schedule_monday_class()

elif CURRENT_DAY == "Wed":
    schedule_wednesday_class()

elif CURRENT_DAY == "Thu":
    schedule_thursday_class()

elif CURRENT_DAY == "Fri":
    schedule_friday_class()

elif CURRENT_DAY == "Sat":
    schedule_friday_class()

else:
    print("Sunday ..... ")
