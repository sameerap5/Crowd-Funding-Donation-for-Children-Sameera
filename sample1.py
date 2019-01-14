from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)   #file location and browser which we will use to open
driver.get("https://www.donorschoose.org/project/time-for-tables/3719662/")
driver.find_element_by_name("https://www.donorschoose.org/donors/search.html").click()


#preferences = {"download:default_directory": "Downloads"}
Options.add_experimental_option("prefs", {"download:default_directory": "D:\USF\Selenium"})

driver = webdriver.chrome(chrome_options=Options)

input1 = driver.find_element_name("textbox").send_keys("message")
driver.find_element_by_xpath("//*[@id='content']/div/div/div/div[2]/div[1]/span[1]/input[2]").click()
driver.find_element_by_id("text").click()
