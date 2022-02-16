import requests
from bs4 import *

animelink = raw_input("https://www1.gogoanime.ai/category/kimetsu-no-yaiba")  #User Enters URL

start = int(input("1"))
end = int(input("26"))
print "1", start, "26", end 
end=end+1 # Increased by 1 for range function

animename = animelink.split("/")  #splits link by /
URL_PATTERN = 'https://www1.gogoanime.ai/{}-episode-{}' #General URL pattern for every anime on gogoanime
for episode in range(start,end):
	url = URL_PATTERN.format(animename[4],episode)
	srcCode = requests.get(url)
	plainText = srcCode.text
	soup = BeautifulSoup(plainText,"lxml")
	source_url = soup.find('div', {'class': 'download-anime'}).find('a')     #get element with 'a' tag
	link = source_url.get('href')
	dowCode = requests.get(link)
	data = dowCode.text
	soup = BeautifulSoup(data,"lxml")
	dow_url = soup.findAll('div', {'class': 'dowload'})[2].find('a')     #get 3rd elements with 'a' tag
	dowlink = dow_url.get('href')
	print dowlink
	f = open('{}.txt'.format(animename[4]),"a") #opens file with name of "test.txt"
	f.write(dowlink+"\n\n")

f.close()
