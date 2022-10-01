


import time
import webbrowser
import os
import array as arr
link = input("video link:  ")
tabs = int(input("tabs in one window:  "))
video = int(input("how much time for video: "))
reopen = int(input("how many times to reopen:  "))
print('''

your default browser

1 chrome
2 firefox
3 exit
	''')

brow = int(input("your browser:  "))


if brow == 1: 

	for x in range(reopen):
		for y in range(tabs):
			webbrowser.open_new_tab(f"{link}");
			time.sleep(2)
	time.sleep(video)
	os.system("taskkill /im f{chrome}.exe /f")
	
if brow == 2: 

	for x in range(reopen):
		for y in range(tabs):
			webbrowser.open_new_tab(f"{link}");
			time.sleep(2)
	time.sleep(video)
	os.system("taskkill /im f{firefox}.exe /f")
	

if brow == 3:
	print("thanks for using")
	quit()
		
# f'"{link}"'