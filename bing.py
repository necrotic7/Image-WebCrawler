import requests
from bs4 import BeautifulSoup
import lxml
import os
import urllib.request
import sys
import json
import random
first=0
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
for count, i in enumerate(range(0,350, 35)):
	first = str(i)
	try:
		r1=requests.get('https://www.bing.com/images/async?q=people+bending&first='+ first +'&mmasync=1', headers=headers) 
	except:
		print('網路錯誤')
		break
	soup=BeautifulSoup(r1.text,'html.parser')

	image=soup.find_all('div', {'class' : ['img_cont hoff']})
	
	print('圈數:',count, first)
	#下面的迴圈是找圖片網址再把結果放到陣列裡
	links=[]
	for d in image:
		if d.find('img'):       #再從div找img裡面的src  
			result=d.find('img')['src']
			links.append(result)
			
	try:
		x=1
		for link in links:
			# print('圖片連結：', link)
			local = os.path.join('/Users/ziv.wu/Desktop/WebCrawler/bing-imgs/bending/%s-%s.jpg' %(count+1, x))
			urllib.request.urlretrieve(link,local) #link是下載的網址 local是儲存圖片的檔案位址
			x+=1
			print('已下載%s-%s.jpg'%(count+1, x))
	except:
		print('下載錯誤')
		continue

print('執行完畢')
		