#
# Download url from the website "https://www.donorschoose.org"
# argv[1]="D:\\USF\Selenium\chromedriver.exe"
# The outcome will be saved with the following name current_date + '.csv' in the same location where the file has been executed 
# The example running script will look like the following:
# python DownloadingUrlFromDonorsWebsite.py "D:\\USF\Selenium\chromedriver.exe" ""
# AuthorName: Sameera Prasad, Vivek Singh
#################################################################################################

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import datetime
import shutil
import os

chromeoptions = Options()
#driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)
#chromeoptions.add_argument('headless')
try:
	driver = webdriver.Chrome(executable_path=argv[1], chrome_options=chromeoptions)

except:
	pass
base_url="https://www.donorschoose.org/donors/search.html?page="
page_counter=1

list_m = []
while(True):
    try:
        now = datetime.datetime.now()
        current_date = now.strftime("%Y%m%d")
        driver.get(base_url+str(page_counter))
        time.sleep(10)
        #all_urls = driver.find_elements_by_xpath("//div[@class='search-results']")
        #div_m=driver.find_elements_by_xpath("//div[@data-reactid='218']")
        all_urls1 = driver.find_elements_by_xpath("//a[@class='project-card']")
        all_urls2 = driver.find_elements_by_xpath("//a[@class='project-card match-dyi with-match']")
        for a in all_urls1:
            # print(a.get_attribute('href'))
            list_m.append(a.get_attribute('href'))
            #b=pd.DataFrame(b)
        for a in all_urls2:
            # print(a.get_attribute('href'))
            list_m.append(a.get_attribute('href'))
            
        print('total urls '+str(len(all_urls1) + len(all_urls2))+'page '+str(page_counter))
        page_counter+=1
        if (page_counter>110):
            break
    except:
         print('')


csvFile=os.path.join(current_date + '.csv')			#file being name with today's date
#os.makedirs(csvFile)				#folder getting created with name destionation hence can be ignored

#csvFile = "ReferenceLinks.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list_m:
        writer.writerow([val])
