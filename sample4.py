
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=chromeoptions)   #file location and browser which we will use to open
base_url="https://www.donorschoose.org/donors/search.html?page="
page_counter=1

list = []
while(True):
    try:
        driver.get(base_url+str(page_counter))
        time.sleep(10)
        all_urls = driver.find_elements_by_xpath("//div[@class='search-results']")
        for a in all_urls[0]:
            # print(a.get_attribute('href'))
            list.append(a.get_attribute('href'))
            #b=pd.DataFrame(b)

            #list.to_csv(csvFile,sep=',')
    except:
        break

csvFile = "sample4.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list:
        writer.writerow([val])