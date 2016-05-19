import requests
import re
import os
import urllib	
from bs4 import BeautifulSoup 
from time import time,sleep
from threading import Thread


def createFolderIfNotExists(name):
	#This creates a particular folder if not exists
	if not os.path.exists(name):
		os.makedirs(name)


def downloadURL(url,name):
	print "Downloading ",name," started"
	startTime = time()
	urllib.urlretrieve(url,name)
	print "Done downloading ",name," in",time()-startTime


createFolderIfNotExists('Popular-Electronics')

requestedPage = requests.get("http://www.americanradiohistory.com/Popular-Electronics-Guide.htm") 
	
ramen = BeautifulSoup(requestedPage.text,"html.parser") 

#You see what i did there with ramen? 

yearWiseList = {} #This will contain the issue names as in 
# yearWiseList = {1999:[all the filename],2000:[all the filenames]} etc

for link in ramen.find_all('a'):
	url = str(link.get('href'))
	if re.search("pdf",url):

		splittedUrl = url.split("/") #Split the url

		filename = splittedUrl[-1]   #select the last part of the url

		yearRegex = re.search(r"[0-9]{4}",filename) #Find the issue year 

		year = filename[yearRegex.start(): yearRegex.end()] #Exctract the issue year

		if not year in yearWiseList:
			yearWiseList[year] = []   #This initializes the year array for a new year. 
			createFolderIfNotExists("Popular-Electronics/"+year)

		yearWiseList[year].append(url)  #Add the issue to the particular year.



for year in yearWiseList:
	directory = "Popular-Electronics/"+year+"/"    #Create the directory path string to be appended
	threads = [Thread(target=downloadURL,args=("http://www.americanradiohistory.com/"+issue,directory+issue.split('/')[-1],)) for issue in yearWiseList[year]]
	#This creates an array of threads for only that year
	for thread in threads:
		thread.start()

	for thread in threads:
		# This stops further process till that thread is done.
		thread.join()

print "done Downloading all"


