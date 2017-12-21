import urllib2
from bs4 import BeautifulSoup
import requests
import re
import csv
import string

quote_page = 'https://www.seek.com.au/jobs'
page = urllib2.urlopen(quote_page)
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

job_list=[]

for i in range(0, len(flag_id)-2):
	 job_list.append(part[flag_id[i]:flag_id[i+1]])

info_list= []

for i in range(0, len(job_list)-1):
	temp_list = []
	temp_str = ""
	temp_str = job_list[i].replace('{','').replace('}','').replace('"','')
	temp_list = re.split('[,:]', temp_str)
	info_list.append(temp_list)
print info_list
with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(info_list)
