import pandas as pd
import re
from langdetect import detect

from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk

from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()

from warnings import warn

url = "https://mail.yahoo.com"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
sleep(8)

driver.find_element_by_xpath("/html/body/div[1]/a[2]/span").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/form/div[1]/div[3]/input").send_keys("amandineberkeunaerts@yahoo.com")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/form/div[2]/input").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input").send_keys("AmandineSuccess!*")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[3]/button").click()
sleep(5)
driver.find_element_by_xpath("/html/body/header/div/div/div/div[1]/div[2]/ul/li[1]/a").click()
sleep(3)

links=[]
for i in range(0,1):
    card = driver.find_elements_by_xpath('//li[@class="H_A hd_n p_a L_0 R_0"]')
    sleep(3)
    
    for mail in card:
        try:
            link=mail.find_element_by_xpath('.//a[@class="D_B bn_dBP bm_FJ bj_ZpQYvz ir3_1JO2M7 I4_1I4yPF"]').get_attribute(name="href")
        except:
            link=' '
        print(link)
        links.append(link)

for i in range(len(links)):
    if(links[i]!=' '):
        driver.get(links[i])
        sleep(8)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/ul/li/div/div/div[1]/div[2]/div/div/div/div/table/tbody/tr/td/center/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[1]/tbody/tr/td/a/table/tbody").click()
            sleep(6)
        except:
            continue;
    else:
        continue;
    