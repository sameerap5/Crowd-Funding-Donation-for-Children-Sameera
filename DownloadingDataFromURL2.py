

# download information from the url generated from the website

#argv[1] is location of chrome driver
#argv[1]="D:\\USF\Selenium\chromedriver.exe"

# Outcome file. File will be saved here 
#argv[2]='D:\\USF\Selenium\ + CurrentDateCsvFile.csv'


import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import pandas as pd
import urllib.request
import datetime
import shutil
import os


chromeoptions=Options
#chromeoptions.add_argument('headless')
try:
	driver = webdriver.Chrome(executable_path=sys.argv[1], chrome_options=chromeoptions)

except:
	pass
time.sleep(10)

fp=open('20190422.csv')
urls=fp.readlines()
data_m=pd.DataFrame()
now = datetime.datetime.now()
current_date = now.strftime("%Y%m%d")
for url in urls:
	try:																								
		driver.get(url)
		time.sleep(10)
		stats = driver.find_elements_by_xpath("//ul[@class='donation-stats clearfix']")   #works perfect
		tmp = stats[0].text.split('\n')
		title = driver.find_elements_by_xpath("//h1[@class='js-title js-project-title']")		#works perfect
		#tmp.append(title[0].text
		tmp.append(h1.get_attribute('href'))

		
		try:
#expiry date
			expiry2 = driver.find_elements_by_xpath("//span[@class='expiration-date']")
			#expiry1 = driver.find_elements_by_xpath("//h4[@class='fully-funded']")
			if(len(expiry2)!=0):
				tmp.append(expiry2[0].text)
				#continue

			expiry3 = driver.find_elements_by_xpath("//h4[@class ='notFunded']")
			if(len(expiry3)!=0):
				tmp.append('No Funding needed')
				#continue



			#elif(len(expiry1)!=0):
			else:

				tmp.append('fully funded')





		except:

			tmp.append('')
		try:
#the link directing to the teacher's information	
			teacher_link = driver.find_elements_by_xpath("//a[@class='teacher-link']")
			teacher_link[0].click()
			time.sleep(10)
		except:
			print(url)
		

#teacher's name
		try:
			teacher_name=driver.find_elements_by_xpath("//a[@class='teacher-link']")						#print the teacher name
			if(len(teacher_name)!=0):
				tmp.append(teacher_name[0].text)
			else:
				tmp.append('')
		except:
			print(url)
		
#Economic descripton

		try:
			eco=driver.find_elements_by_xpath("//li[@class='economic-descriptor']")				#leconomic-descriptor end statememtns of the class
			tmp.append(eco[0].text)
		except:
			tmp.append('')
			time.sleep(7)
		
#Details of the school
		try:
			loc=driver.find_elements_by_xpath("//div[@id='school-details-all']")				#location of the class not working!
			if(len(loc)!= 0):
				tmp.append(loc[0].text)
			else:
				tmp.append('')
		except:
			print(url)
#location of the school
		try:
			nbutton=driver.find_elements_by_xpath("//span[@class='school-location']")
			print(nbutton.text)
			tmp.append(nbutton[0].text)
				
		except:
			tmp.append('')

		# try:
		# 	teacher_img=driver.find_element_by_xpath("//a[@class='classroom-photo js-classroom-photo-format-retina-bg ']")
		# 	tmp.append(teacher_img[0].text)
		# except:
		# 	tmp.append('')

		# image_element = driver.find_elements_by_xpath("//a[@class='classroom-photo js-classroom-photo-format-retina-bg ']")  #image extraction
		# image_url = 'http:' + image_element[0].get_attribute('style').split(':')[2].split('"')[0]
		# file_name = url.split('/')[-2] + '.png'
		# urllib.request.urlretrieve(image_url, file_name)




		#with open('filename.png', 'wb') as writer:  # open for writing in binary mode
			#writer.write(img.content)  # write the image

		#don_goes=driver.find_element_by_xpath("//h2 [@class='desktop js-materials']")
		#tmp.append(don_goes[0].text)

		#don_goes = driver.find_element_by_id("//a[@class='teacher-school']")
		#tmp.append(don_goes[0].text)    						#web element does not support indexing



		#pro_act=driver.find_element_by_xpath("//h2 [@class='desktop ']")
		#tmp.append(pro_act[0].text)


#storing it in a dataframe


#giving titles to the columns
		header_list = ['Donors', 'Donors still needed', 'Goal','Title','Expiry', 'Teacher Name', 'Descriptor', 'Location']
		data_m=data_m.reindex(columns=header_list)
		if(tmp[2]=='No Funding needed'):
			data_m = data_m.append({'Donors': "", 'Donors still needed': "", 'Goal': tmp[0], 'Title': tmp[1], 'Expiry': "No funding needed",  'Teacher Name' : tmp[3], 'Descriptor':tmp[4], 'Location' :tmp[5]},ignore_index=True)  # avalues getting added here
	
		elif(tmp[3]=='fully funded'):
			data_m = data_m.append({'Donors': tmp[0], 'Donors still needed': "", 'Goal': tmp[1], 'Title': tmp[2], 'Expiry': "fully funded",'Teacher Name' : tmp[4],  'Descriptor':tmp[5], 'Location' : tmp[6]},ignore_index=True)  # avalues getting added here

		else:
			data_m = data_m.append({'Donors': tmp[0], 'Donors still needed': tmp[1], 'Goal': tmp[2], 'Title': tmp[3], 'Expiry': tmp[4],  'Teacher Name' : tmp[6],  'Descriptor':tmp[7], 'Location' : tmp[8]}, ignore_index=True)   #avalues getting added here
	except:
		print(url)
#time.sleep(10)
#data_m.to_csv('D:\\USF\Selenium\Datadonors1.csv')
csvFile=os.path.join(current_date + 'Information'+'.csv')
data_m.to_csv(sys.argv[2]+csvFile, sep='\t', encoding='utf-8')	
