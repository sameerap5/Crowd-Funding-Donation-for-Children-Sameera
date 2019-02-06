# download pages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import pandas as pd
import urllib.request

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)
#chromeoptions.add_argument('headless')
# try:
	# driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)

# except:
	# pass
time.sleep(10)

fp=open('sample_11.csv')
urls=fp.readlines()
data_m=pd.DataFrame()
for url in urls:
	try:
		driver.get(url)
		time.sleep(10)
		stats = driver.find_elements_by_xpath("//ul[@class='donation-stats clearfix']")   #works perfect
		tmp = stats[0].text.split('\n')
		title = driver.find_elements_by_xpath("//h1[@class='js-title js-project-title']")		#works perfect
		tmp.append(title[0].text)

		#sam codes
		try:

			expiry2 = driver.find_elements_by_xpath("//span[@class='expiration-date']")
			#expiry1 = driver.find_elements_by_xpath("//h4[@class='fully-funded']")
			if(len(expiry2)!=0):
				tmp.append(expiry2[0].text)

			expiry3 = driver.find_elements_by_xpath("//h4[@class ='notFunded']")
			if(len(expiry3)!=0):
				tmp.append('No Funding needed')



			#elif(len(expiry1)!=0):
			else:

				tmp.append('fully funded')





		except:

			tmp.append('')
		try:
	
			teacher_link = driver.find_elements_by_xpath("//a[@class='teacher-link']")
			teacher_link[0].click()
		except:
			print(url)
		

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


#sam addition ends


		header_list = ['Donors', 'Donors still needed', 'Goal','Title','Expiry', 'Funding']
		data_m=data_m.reindex(columns=header_list)
		if(tmp[2]=='No Funding needed'):
			data_m = data_m.append({'Donors': "", 'Donors still needed': "", 'Goal': tmp[0], 'Title': tmp[1], 'Expiry': "", 'Funding' : "no funding needed"},ignore_index=True)  # avalues getting added here

		elif(tmp[3]=='fully funded'):
			data_m = data_m.append({'Donors': tmp[0], 'Donors still needed': "", 'Goal': tmp[1], 'Title': tmp[2], 'Expiry': tmp[3],'Funding' : "" },ignore_index=True)  # avalues getting added here

		else:
			data_m = data_m.append({'Donors': tmp[0], 'Donors still needed': tmp[1], 'Goal': tmp[2], 'Title': tmp[3], 'Expiry': tmp[4], 'Funding': ""}, ignore_index=True)   #avalues getting added here
	except:
		print(url)
#time.sleep(10)
data_m.to_csv('D:\\USF\Selenium\Datadonors.csv')
print(data_m)
