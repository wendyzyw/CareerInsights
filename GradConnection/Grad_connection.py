import urllib2
from bs4 import BeautifulSoup
import requests
import re
import csv

def findOccurences(s, ch):
	return [i for i, letter in enumerate(s) if letter == ch]

def remove_prefix(text, prefix):
	if text.startswith(prefix):
		return text[len(prefix):]
	return text

def output_all_info_in_urls(url,file_name):
	page_gra = urllib2.urlopen(url)
	soup_graduate_jobs = BeautifulSoup(page_gra, 'html.parser')
	html = list(soup_graduate_jobs.children)[2]
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
	for i in range(0, len(position1)-1):
		list1.append(part[position1[i]:position2[i]])
	list_diced = []
	for i in range(0, len(list1)-1):
		list_temp = []
		temp = []
		temp = findOccurences(list1[i], ",")
		for j in range(0, len(temp)-2):
			list_temp.append(list1[i][temp[j]:temp[j+1]])
		list_temp.append(list1[i][(temp[len(temp)-1]):(len(list1[i])-1)])
		list_diced.append(list_temp)

	with open("%s_output.csv" %file_name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(list_diced)
	return part

def find_all_urls(string, file_name):
	url_position = []
	url_position = [m.start() for m in re.finditer('url', string)]
	url_list = []
	for i in range(0, len(url_position)-1):
		temp = ''
		j = url_position[i]
		while string[j] != ',':
			temp = temp + string[j]
			j = j+1
		url_list.append(temp)

	for elem in url_list[:]:
		if len(elem) <= 10:
			url_list.remove(elem)

	for i in range(0, len(url_list)-1):
		url_list[i] = remove_prefix(url_list[i], "url\":")

	with open("url_in_%s.csv" %file_name, "wb") as f:
		writer = csv.writer(f)
		writer.writerow(url_list)


graduate_jobs = 'https://au.gradconnection.com/graduate-jobs/'
string = ''
string = output_all_info_in_urls(graduate_jobs, "graduate_jobs")
find_all_urls(string, "graduate_jobs")

internships = 'https://au.gradconnection.com/internships/'
string = ''
string = output_all_info_in_urls(internships, "internships")
find_all_urls(string, "internships")

part_time = 'https://au.gradconnection.com/part-time-student-jobs/'
string = ''
string = output_all_info_in_urls(part_time, "part_time")
find_all_urls(string, "part_time")

entry_level = 'https://au.gradconnection.com/entry-level-jobs/'
string = ''
string = output_all_info_in_urls(entry_level, "entry_level")
find_all_urls(string, "entry_level")

clerkship = 'https://au.gradconnection.com/clerkships/'
string = ''
string = output_all_info_in_urls(clerkship, "clerkship")
find_all_urls(string, "clerkship")

scholarships = 'https://au.gradconnection.com/scholarships/'
string = ''
string = output_all_info_in_urls(scholarships, "scholarships")
find_all_urls(string, "scholarships")

