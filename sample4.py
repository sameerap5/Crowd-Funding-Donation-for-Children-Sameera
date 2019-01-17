
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)   #file location and browser which we will use to open
driver.get("https://www.donorschoose.org/donors/search.html")

csvFile = "D:\\USF\Selenium\sample4.csv"
list = []
for a in driver.find_elements_by_xpath('.//a'):
   # print(a.get_attribute('href'))
    list.append(a.get_attribute('href'))
    #b=pd.DataFrame(b)

#list.to_csv(csvFile,sep=',')

with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list:
        writer.writerow([val])