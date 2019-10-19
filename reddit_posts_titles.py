#Rini94
#Gets the titles of the last few posts on subreddit
#Arguments: First argument is subreddit name, default is homepage; second is sort type, default is hot
import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/"
if len(sys.argv) > 1:
	url = url + "r/" + sys.argv[1]
if len(sys.argv) > 2:
	url = url + "/" + sys.argv[2]

print("Loading...")

page = requests.get (url, headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'})
if page.status_code == 200:
	soup = BeautifulSoup (page.content, 'html.parser')
	post_titles = soup.body.find_all("a", {"data-click-id":"body"})
	for post in post_titles:
		print("\n" + post.getText())
	print("\n")
else:
	print ("Failed")