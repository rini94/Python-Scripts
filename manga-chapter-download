#Web scraping test - download manga pages and save to folder
#Rini94
#Mangafox - download single chapter

import requests
import urllib.request
import sys
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

page_count = 0
max_count = 100 #total downloads/download attempts at a single run
fail_count = 0
count = 0

image_chapter = None

def download_image(image):
	try:
		image_url = image.get_attribute('src')
		print (image_url)

		name = image_url.split('?')
		name1 = name[0].split('/')
		image_name = name1[len(name1) - 1]
		chapter = name1[len(name1) - 3]

		global image_chapter
		if image_chapter == None:
			image_chapter = chapter
		elif image_chapter != chapter:
			print ("image_chapter", image_chapter)
			return "next_chapter"

		if ".jpg" in image_url:
			urllib.request.urlretrieve(image_url, image_name)
			print ("downloaded image from: ", image_url)
			return "success"
		else:
			print ("failure", page_count)
			driver.implicitly_wait(1)

	except Exception as e:
		print ("Exception", e)
		driver.implicitly_wait(1)

chapter_url = input ("Enter the main url of the chapter: \n")

if len(chapter_url) <= 1:
	print ("\nNo chapter url entered...\nExiting...\n")
	sys.exit()

if not chapter_url.endswith ("/"):
	chapter_url = chapter_url + "/"
chapter_url = chapter_url + "1.html"

print ("\nLoading...\n")
print ("\nchapter_url: ", chapter_url)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(chapter_url)

chapter = chapter_url.split('/')
chapter_name = chapter[len(chapter) - 2]

file_path = os.path.dirname(os.path.realpath(__file__))+ "/"+chapter_name+"/"
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
	os.makedirs(directory)
os.chdir(file_path)

print("directory: ",os.getcwd())

while count + fail_count < max_count:
	image = driver.find_element_by_class_name("reader-main-img")
	download = download_image(image) #download a single image
	if download == "success":
		count = count + 1
		image.click()
	elif download == "next_chapter":
		break
	else:
		fail_count = fail_count + 1

print ("total failures: ", fail_count)
print ("total successes: ", count)
print ("Completed")

sys.exit()
