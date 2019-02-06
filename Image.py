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
#driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)
chromeoptions.add_argument('headless')
try:
	driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)

except:
	pass
#time.sleep(10)

fp=open('error_remained_image.csv')
urls=fp.readlines()
data_m=pd.DataFrame()
for url in urls:
	try:
		driver.get(url)
#time.sleep(10)
		
		image_element = driver.find_elements_by_xpath("//a[@class='classroom-photo js-classroom-photo-format-retina-bg ']")  #image extraction
		image_url = 'http:' + image_element[0].get_attribute('style').split(':')[2].split('"')[0]
		file_name = url.split('/')[-2] + '.png'
		urllib.request.urlretrieve(image_url, file_name)
	except:
		print(url)
		
	#except:
		#print(url)
#time.sleep(10)
#data_m.to_csv('D:\\USF\Selenium\DataImage')
