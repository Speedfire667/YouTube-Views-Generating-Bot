'''
Subscribe `Fauceter' Now :) https://www.youtube.com/channel/UCqmC9XrDnoihqqiiCOnPwDg
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = str(input('https://youtu.be/7koPZ165-IM?si=gaPuYQNE_-nVXSiW'))
DRIVERS = int(input('1'))
driver = []
BreakRate = 10 #sec
PATH = 'C:\Program Files (x86)\chromedriver.exe' #path of chromedriver

for i in range(DRIVERS):
    driver.append(webdriver.Chrome(PATH))
    driver[i].get(URL)
    action = ActionChains(driver[i])
    action.send_keys(Keys.SPACE)
    action.perform()
        
while True:
    time.sleep(BreakRate)
    for j in range(DRIVERS):
        driver[j].refresh()
        action = ActionChains(driver[j])
        action.send_keys(Keys.SPACE)
        action.perform()

