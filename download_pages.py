# download pages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import pandas as pd

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=chromeoptions) 
time.sleep(10)

fp=open('sample4.csv')
urls=fp.readlines()
data_m=pd.DataFrame()
for url in urls:
	try:
		driver.get(url)
		time.sleep(10)
		stats = driver.find_elements_by_xpath("//ul[@class='donation-stats clearfix']")
		tmp=stats[0].text.split('\n')
		title=driver.find_elements_by_xpath("//h1[@class='js-title js-project-title']")
		tmp.append(title[0].text)

		header_list=['Donors','Donors still needed', 'goal','title']
		data_m=data_m.reindex(columns=header_list)
		data_m = data_m.append({'Donors':tmp[0], 'Donors still needed':tmp[1],'goal':tmp[2],'title':tmp[3]}, ignore_index=True)
		
		
		#*******************sam additional codes
		#try:
		#	expiry=driver.find_element_by_xpath("//p[@class='undefined-sticky-wrapper']")
		#	tmp.append(expiry[0].text)
		#except:
		try:													#funding scenario
			expiry1 = driver.find_element_by_xpath("//h4[@class='fully-funded']")
			expiry2 = driver.find_element_by_xpath("//p[@class='text-discreet']")
			for a in expiry1:
				tmp.append(expiry1[0].text)
			for a in expiry2:
				tmp.append(expiry2[0].text)
			#expiry = expiry1 + expiry2
		except:		#	tmp.append('')
		

		#teacher_img=driver.find_element_by_xpath("//a[@class='classroom-photo js-classroom-photo-format-retina-bg']")
		#tmp.append(teacher_img[0].text)

		#don_goes=driver.find_element_by_xpath("//h2 [@class='desktop js-materials']")
		#tmp.append(don_goes[0].text)

		#don_goes = driver.find_element_by_xpath("//td [@class='itemName']")
		#tmp.append(don_goes[0].text)    						#web element does not support indexing



		#pro_act=driver.find_element_by_xpath("//h2 [@class='desktop ']")
		#tmp.append(pro_act[0].text)


#****************sam addition ends
		image_element = driver.find_elements_by_xpath("//a[@class='classroom-photo js-classroom-photo-format-retina-bg ']")

		image_url = 'http:' + image_element[0].get_attribute('style').split(':')[2].split('"')[0]
		count=1

		import urllib.request
		for img in image_url:

			file_name = 'filename' + str(count) + '.png'
			count += 1

			urllib.request.urlretrieve(image_url, file_name)

		header_list=['Donors','Donors still needed', 'goal','title','expiry','donation_goes','teacher_img','don_goes','pro_act']
		data_m=data_m.reindex(columns=header_list)
		data_m = data_m.append({'Donors':tmp[0], 'Donors still needed':tmp[1],'goal':tmp[2],'title':tmp[3], 'expiry':tmp[4],'teacher_img':tmp[5],'don_goes':tmp[6] , 'pro_act':tmp[7]}, ignore_index=True)   #avalues getting added here
	except:
		

		print(url)
data_m.to_csv('data.csv')
	
	
	

