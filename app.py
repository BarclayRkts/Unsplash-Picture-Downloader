from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, shutil, glob, time

def getImages(pic_name):
    driver = webdriver.Chrome()
    driver.get('https://unsplash.com/')
    time.sleep(2)

    # search
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[1]/form/div/input')
    search.click()
    search.send_keys(pic_name)
    time.sleep(2)
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    pic = driver.find_element_by_class_name('nDTlD')
    pic.click()
    time.sleep(2)

    for picture in range(0, 10):
        time.sleep(1)
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/a') # click the next button
        element.click()
        time.sleep(2)
        driver.find_element_by_class_name('_2vsJm').click() # download the image

    time.sleep(10)

def downloadImages():
    file_location = " " # the location that files are downloaded to. Mostly the downloads for folder on windows/mac
    
    try:
        os.mkdir(" ")  #    location that you want store your picture file in
    except:
        print("error. Folder already exists")
    
    move_location = " "       #    location that you want store your picture file in. Same location as mkdir in the try statement

    for item in range(0, 10):
        list_of_files = glob.glob(file_location + '\\*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        shutil.move(latest_file, move_location) #move to new folder
        print (latest_file)


pic_name = input("What type of pictures do you want to search for? ")
getImages(pic_name)
downloadImages()

