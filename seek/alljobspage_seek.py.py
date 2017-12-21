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

with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(info_list)
'''
with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(row_list)
'''
'''
for word in temp_str:
		print word
		temp.append(word)
	row_list.append(temp)
'''
'''
for char in job_list[i]:
		if char in '}"{':
			temp_str = job_list[i].replace(char, '')
'''
'''
word_list[][] = ""
for i in range(0, len(job_list)-1):
	word_list[i].append(job_list[i].split(","))

replace_punctuation = string.maketrans(string.punctuation,' '*len(string.punctuation))
	temp_str = job_list[i].translate(replace_punctuation)
	temp = re.split('\s+',temp_str)
	row_list.append(temp)
'''
'''

'''
'''
with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(job_list)
'''
