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
	except:
		print(url)
data_m.to_csv('data.csv')
	
	
	

