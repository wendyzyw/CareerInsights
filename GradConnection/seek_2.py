import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import csv

def findOccurences(s, ch):
	return [i for i, letter in enumerate(s) if letter == ch]

seek = 'https://www.seek.com.au/jobs'
page = urlopen(seek)
soup = BeautifulSoup(page, 'html.parser')
html = list(soup.children)[2]
body = list(html.children)[3]
body_part = []
for x in body:
	body_part.append(str(x))
part = ''.join(body_part)

position1 = []
position1 = findOccurences(part, '{')
position2 = []
position2 = findOccurences(part, '}')
list1 = []

for i in range(0, len(position1)):
	list1.append(part[position1[i]: position2[i]])



with open("try_2.csv", "w", encoding="utf8") as f:
	writer = csv.writer(f)
	for item in list1:
		writer.writerow([item])
