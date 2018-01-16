import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import csv



def decode_url(list):
	for i in range(0, len(list)):
		print(urllib.parse.unquote(list[i]))

list= ['\u002Fapi\u002Fcountries\u002FAU', 'https:\u002F\u002Fbit.ly\u002F2jVUTRk','http:\u002F\u002Fau.gradconnection.com\u002Fapi\u002Fcustomerorganizationlist\u002Fd5691f3b-068b-4e5f-a05c-a38f508fbcda\u002F', 'https:\u002F\u002Fbit.ly\u002F2invnUN']
decode_url(list)
print(type(list[1]))