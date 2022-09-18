


import time
import webbrowser
import os
import array as arr
link = input("video link:  ")
tabs = int(input("tabs in one window:  "))
video = int(input("how much time for video: "))
reopen = int(input("how many times to reopen:  "))
print('''

if you use chrome write "chrome"

if you use firefox write "firefox"
	''')

brow = input("your browser:  ")





for x in range(reopen):
	for y in range(tabs):
		webbrowser.open_new_tab(f"{link}");
		time.sleep(2)
	time.sleep(video)
	os.system("taskkill /im f{brow}.exe /f")
	
		
# f'"{link}"'
