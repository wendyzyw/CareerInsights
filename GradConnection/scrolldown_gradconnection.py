import urllib
from selenium import webdriver
import time

from bs4 import BeautifulSoup
import requests

import string
import re
import csv
import selenium
driver = webdriver.Chrome(executable_path=r"C:\Chrome\chromedriver.exe")
driver.get('https://au.gradconnection.com/graduate-jobs/')
driver.execute_srcipt("window.scrollTo(0, document.body.scrollHeight);")

result_raw = driver.page_source
result_soup = BeautifulSoup(result_soup, 'html.parser')
result_bf = result_soup.prettify()
print(result_soup)