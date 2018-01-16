import csv
import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import csv

url = []
url.append('http:\u002F\u002Fau.gradconnection.com\u002Fapi\u002Fdemographics\u002F73e7e18b-57fe-4b46-9796-5a495ba3f33e\u002F')
url.append('http:\u002F\u002Fau.gradconnection.com\u002Fapi\u002Fdemographics\u002Fd5ae17e5-5c52-4779-9241-5d7fc28856b1\u002F')
url.append('http:\u002F\u002Fau.gradconnection.com\u002Fapi\u002Fdemographics\u002Ff61278e3-e843-4ab4-9e1e-fcf17a58480a\u002F')

dec_url = []
for i in range(0,3):
	dec_url.append(urllib.parse.unquote(url[i]))

with open("try.csv", "w", encoding="utf8") as f:
	writer = csv.writer(f)
	writer.writerow(dec_url)

