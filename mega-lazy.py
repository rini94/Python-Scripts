import webbrowser
import pyperclip
import base64
import re

content = pyperclip.paste()
content_arr = re.split(r'(\s+)', content)

big_one = ""
max_len = 0
word_len = 0
second_len = 0

for word in content_arr:
	word_len = len (word)
	if word_len > max_len:
		max_len = word_len
		big_one = word
	elif word_len > second_len:
		second_len = word_len
		big_two = word

try:
	print('Text from clipboard: ' + content)
	
	if len(big_one) > 60:
		print ('Encoded url: ' + big_one)
		url = base64.b64decode (big_one)
	else:
		dec_url_one = base64.b64decode (big_one)
		dec_url_two = base64.b64decode (big_two)
		if 'mega' in dec_url_one:
			print ('Encoded url - link: ' + big_one)
			print ('Encoded url - key: ' + big_two)
			url = dec_url_one + dec_url_two
		else:
			print ('Encoded url - link: ' + big_two)
			print ('Encoded url - key: ' + big_one)
			url = dec_url_two + dec_url_one

	print ('Decoded url: ' + url)

	webbrowser.open_new_tab(url)
except:
	print ('Error ocurred while decoding... Please check your copied content.')