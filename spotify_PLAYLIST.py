
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains 
from config import Config
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/div/input').send_keys(f'{Config.USERNAME}')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/div/input').send_keys(f'{Config.PASSWORD}')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/div[2]/button').click()
time.sleep(10)
driver.get(f'{Config.link_OF_PLAYLIST}')
time.sleep(10)
added_songs=[]
nofsongs=Config.NO_OFSONGS
def getSongs():
    global added_songs
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[4]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]').click()
    time.sleep(10)
    print(driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/footer/div/div[1]/div').get_attribute("aria-label"))
    added_songs.append(driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/footer/div/div[1]/div').get_attribute("aria-label"))
    driver.find_element_by_xpath('/html/body/div[11]/div[3]/div/div/div[2]/button').click()
    for i in range (1,nofsongs):
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/button[4]').click()
        time.sleep(10)
        print(driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/footer/div/div[1]/div').get_attribute("aria-label"))
        added_songs.append(driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/footer/div/div[1]/div').get_attribute("aria-label"))
def convertToText():
    for x in range(0,len(added_songs)):
        song=added_songs[x]
        song = song[12:]#remove 'Now Playing:'
        added_songs[x]=song
    with open('ALL__LIKED_SONGS.txt', 'w') as f:
        for item in added_songs:
            f.write("%s\n" % item)

getSongs()
convertToText()
            
        
    
        