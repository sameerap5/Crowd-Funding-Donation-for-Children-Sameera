# download pages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=chromeoptions) 

fp=open('sample4.csv')
urls=fp.readlines()

for url in urls:
	driver.get(url)
	page = driver.page_source
	file_ = open( url.split('/')[-2]+'_page.html', 'w')
	file_.write(page)
	file_.close()