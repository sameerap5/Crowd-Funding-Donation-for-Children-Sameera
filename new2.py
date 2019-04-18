from bs4 import BeautifulSoup
import urllib.request

import wget

fp=open('sample4.csv')
urls_m=fp.readlines()
fp.close()
base_url="https://www.donorschoose.org/donors/search.html?page="
page_counter=1

for url_m in urls_m:
    

    file_name =   'D:\\USF\Selenium\\HTML_28.03links\\'+url_m.split('/')[-3]+ url_m.split('/')[-2] + '.html'
	
		#wget.download(file_name)
    wget.download(url_m,file_name)
	#err.to_csv(wget.download(url_m,file_name))
	#print(err)
	
	# page = requests.get('file:///D:/USF/Selenium/html1/3rd-grade-crews-overnight-expedition3875150.html')
	#soup = BeautifulSoup(page.content, 'html.parser')
	#for rank in soup.find_all("div", "class"= "donation-stats clearfix"):
		#print(rank)
		
	
	
	
	
	

	