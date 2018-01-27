import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import csv
import os

urls = ["https://www.seek.com.au/jobs?page={}".format(i) for i in range(90, 100)]
filename = 'seek50page.csv'
with open(filename, 'w', encoding='utf8') as f:
	writer = csv.writer(f)

for url in urls:
	page = urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	section = soup.body.find_all('script', {'data-automation':'server-state'})
	content = []
	for item in section:
		content.append(str(item))
	flag = []
	for m in re.finditer('jobs', content[0]):
		flag.append(m.start())
	part = content[0][flag[4]:flag[5]]
	flag_id = []
	for m in re.finditer('id', part):
		flag_id.append(m.start())

	job_list = []
	for i in range(0, len(flag_id)-2):
		job_list.append(part[flag_id[i]:flag_id[i+1]])
	info_list = []
	for i in range(0, len(job_list)-1):
		temp_list = []
		temp_str = ""
		temp_str = job_list[i].replace('{','').replace('}','').replace('"','')
		temp_list = re.split('[,:]', temp_str)
		info_list.append(temp_list)
	with open(filename, 'a', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerows(info_list)


