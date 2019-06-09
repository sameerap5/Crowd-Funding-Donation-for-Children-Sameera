#this file is similar to the to ToObtainURLs2. Hence please consider the file ToObtainURL2 in the github.
#Author: Sameera Prasad, Vivek Singh

######################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import sys

#argv[1]="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe"

chromeoptions = Options()
driver = webdriver.Chrome(executable_path=argv[1], chrome_options=chromeoptions)   #file location and browser which we will use to open
base_url="https://www.donorschoose.org/donors/search.html?page="
page_counter=1

list_m = []
while(True):
    try:
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
            #b=pd.DataFrame(b)

            #list.to_csv(csvFile,sep=',')
        print('total urls '+str(len(all_urls1) + len(all_urls2))+'page '+str(page_counter))
        page_counter+=1
        if (page_counter>110):				#there are 110 pages on the website
            break
    except:
        break

csvFile = "URLsObatined.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list_m:
        writer.writerow([val])
