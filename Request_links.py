import requests
from bs4 import BeautifulSoup


def request_links(url):
	links=[]
	try:
		website = requests.get(url)
		web_text = website.text
		soup = BeautifulSoup(web_text,features="html.parser")
		for nextlink in soup.find_all('a'):
			links.append(nextlink.get('href'))
		for item in links:
			if(item[0] in 'h'):
				print(item)
			else :
				print(url[0:len(url)-1]+"/"+item)
	except:
		print ("Either website not found or worng url")
	

if __name__=='__main__':
	try:
		number =int(input('enter the number of sites?'))
		
		while(number >0):
			number-=1
			link=input('enter the website url')
			request_links(link)
	except:
		print("input must be a number")
	
	