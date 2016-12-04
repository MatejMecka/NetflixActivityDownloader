# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser
import time
import os
import sys
import codecs

def getmovies():
    print "This is for the Google Code In 2016 Task by CCExtractor Netflix: Download the list of content you've already seen"
    username = raw_input('Enter your username: ')
    password = raw_input('Enter your password here: ')
    url = 'https://www.netflix.com/viewingactivity'
    browser = webdriver.Firefox()
    browser.get(url)
    emailElem = browser.find_element_by_name('email')
    emailElem.send_keys(username)
    passElem = browser.find_element_by_name('password')
    passElem.send_keys(password)
    passElem.submit()
    if browser.current_url != url:
        print "ERROR: IDK probably no Internet connection or you forgot to type something or you entered the wrong credentials"
        browser.close()
        sys.exit(1)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #Thanks Prabhjot Rai
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    print "Don't worry about seeing all this movies and dates in the console! You'll soon have them at netflix_activity.txt"
    file = codecs.open('netflix_activity.txt', 'w+', encoding='utf8')
    for movie in browser.find_elements_by_class_name('retableRow'):
        date = movie.find_elements_by_tag_name('div')[0]
        movienameelem = movie.find_elements_by_tag_name('div')[1]
        moviename = movienameelem.text
        print date.text + ': ' + moviename + '\n'
        file.write(date.text + ': ' + moviename + '\n')

    file.close()
    browser.close()
    print "Done"
    print "Exiting ..."

getmovies()
