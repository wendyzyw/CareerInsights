import csv
import re

csv_row = []

count_engineering = 0
count_accounting = 0
count_art = 0
count_finance = 0
count_architecture = 0
count_agriculture = 0
count_administration = 0
count_commerce = 0
count_conslting = 0
count_IT = 0 #computer science + software + Information Technology
count_hospitality = 0
count_science = 0
count_marketing = 0
count_law = 0
count_math = 0
count_medicine = 0
count_insurance = 0
count_communication = 0
count_retail = 0
count_mining = 0
count_customer_service = 0

#for seek. if for other websites, change the filename list
filename = ['seekpage1-9.csv', 'seekpage10-19.csv', 'seekpage20-29.csv', 'seekpage30-39.csv', 'seekpage40-49.csv', 'seekpage50-59.csv', 'seekpage60-69.csv', 'seekpage70-79.csv','seekpage80-89.csv','seekpage90-99.csv']
for file in filename:
	with open(file, 'r', encoding = 'utf8') as f:
		reader = csv.reader(f)
		csv_row.extend(list(reader))


for i in range(0, len(csv_row)):
	flag_engineering = 0
	flag_accounting = 0
	flag_art = 0
	flag_finance = 0
	flag_architecture = 0
	flag_agriculture = 0
	flag_administration = 0
	flag_commerce = 0
	flag_conslting = 0
	flag_IT = 0 
	flag_hospitality = 0
	flag_science = 0
	flag_marketing = 0
	flag_law = 0
	flag_math = 0
	flag_medicine = 0
	flag_insurance = 0
	flag_communication = 0
	flag_retail = 0
	flag_mining = 0
	flag_customer_service = 0
	for j in range(0, len(csv_row[i])):
		if re.search('engineering', csv_row[i][j], re.IGNORECASE):
			flag_engineering = 1
		if re.search('accounting', csv_row[i][j], re.IGNORECASE):
			flag_accounting = 1
		if re.search('art', csv_row[i][j], re.IGNORECASE):
			flag_art = 1
		if re.search('finance', csv_row[i][j], re.IGNORECASE):
			flag_finance = 1
		if re.search('architecture', csv_row[i][j], re.IGNORECASE):
			flag_architecture = 1
		if re.search('agriculture', csv_row[i][j], re.IGNORECASE):
			flag_agriculture = 1
		if re.search('administration', csv_row[i][j], re.IGNORECASE):
			flag_administration = 1
		if re.search('commerce', csv_row[i][j], re.IGNORECASE):
			flag_commerce = 1
		if re.search('consulting', csv_row[i][j], re.IGNORECASE):
			flag_conslting = 1
		if re.search('computer science', csv_row[i][j], re.IGNORECASE) or re.search('Communication Technology',csv_row[i][j],re.IGNORECASE) or re.search('software', csv_row[i][j], re.IGNORECASE) or re.search('Internet Technology', csv_row[i][j], re.IGNORECASE):
			flag_IT = 1
		if re.search('hospitality', csv_row[i][j], re.IGNORECASE):
			flag_hospitality = 1
		if re.search('hospitality', csv_row[i][j], re.IGNORECASE):
			flag_science = 1
		if re.search('hospitality', csv_row[i][j], re.IGNORECASE):
			flag_hospitality = 1
		if re.search('science', csv_row[i][j], re.IGNORECASE):
			flag_science = 1
		if re.search('marketing', csv_row[i][j], re.IGNORECASE):
			flag_marketing = 1
		if re.search('law', csv_row[i][j], re.IGNORECASE):
			flag_law = 1
		if re.search('math', csv_row[i][j], re.IGNORECASE):
			flag_math = 1
		if re.search('medicine', csv_row[i][j], re.IGNORECASE):
			flag_medicine = 1
		if re.search('insurance', csv_row[i][j], re.IGNORECASE):
			flag_insurance = 1
		if re.search('communication', csv_row[i][j], re.IGNORECASE):
			flag_communication  = 1
		if re.search('retail', csv_row[i][j], re.IGNORECASE):
			flag_retail = 1
		if re.search('mining', csv_row[i][j], re.IGNORECASE):
			flag_mining = 1
		if re.search('customer service', csv_row[i][j], re.IGNORECASE):
			flag_customer_service = 1
	if flag_engineering:
		count_engineering += 1
	if flag_accounting:
		count_accounting += 1
	if flag_art:
		count_art += 1
	if flag_finance:
		count_finance += 1
	if flag_architecture:
		count_architecture += 1
	if flag_agriculture:
		count_agriculture += 1
	if flag_administration:
		count_administration += 1
	if flag_commerce:
		count_commerce += 1
	if flag_conslting:
		count_conslting += 1
	if flag_IT:
		count_IT += 1
	if flag_hospitality:
		count_hospitality += 1
	if flag_science:
		count_science += 1
	if flag_marketing:
		count_marketing += 1
	if flag_law:
		count_law += 1
	if flag_math:
		count_math += 1
	if flag_medicine:
		count_medicine += 1
	if flag_insurance:
		count_insurance += 1
	if flag_communication:
		count_communication += 1
	if flag_retail:
		count_retail += 1	
	if flag_mining:
		count_mining += 1
	if flag_customer_service:
		count_customer_service += 1
with open("output.txt", "w") as text_file:
	text_file.write("Engineering job count: %d\nAccounting job count: %d\nArt job count: %d\nFinance job count: %d\nArchitecture job count: %d\nAgriculture job count: %d\nadministration job count: %d\nCommerce job count: %d\nConsulting job count: %d\nIT job count: %d\nHospitality job count: %d\nScience job count: %d\nMarketing job count: %d\nLaw job count: %d\nMath job count: %d\nMedicine job count: %d\nInsurance job count: %d\nCommunication job count: %d\nRetail job count: %d\nMining job count: %d\ncustomer Service job count: %d\n" 
 %(count_engineering, count_accounting, count_art, count_finance, count_architecture, count_agriculture, count_administration, count_commerce, count_conslting, count_IT, count_hospitality, count_science, count_marketing, count_law, count_math, count_medicine, count_insurance, count_communication, count_retail, count_mining, count_customer_service))


print ('Engineering job count: %d' %count_engineering)
print ('Accounting job count: %d' %count_accounting)
print ('Art job count: %d' %count_art)
print ('Finance job count: %d' %count_finance)
print ('Architecture job count: %d' %count_architecture)
print ('Agriculture job count: %d' %count_agriculture)
print ('administration job count: %d' %count_administration)
print ('Commerce job count: %d' %count_commerce)
print ('Consulting job count: %d' %count_conslting)
print ('IT job count: %d' %count_IT)
print ('Hospitality job count: %d' %count_hospitality)
print ('Science job count: %d' %count_science)
print ('Marketing job count: %d' %count_marketing)
print ('Law job count: %d' %count_law)
print ('Math job count: %d' %count_math)
print ('Medicine job count: %d' %count_medicine)
print ('Insurance job count: %d' %count_insurance)
print ('Communication job count: %d' %count_communication)
print ('Retail job count: %d' %count_retail)
print ('Mining job count: %d' %count_mining)
print ('customer Service job count: %d' %count_customer_service)