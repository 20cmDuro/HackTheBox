# "Eternal Loop" - HTB
# @JhinScripter

import zipfile

cur_file = "6969.zip"
cur_zipfile = zipfile.ZipFile(cur_file, "r")

with open("rockyou.txt", "r") as wl:
	for l in wl:
		w = l.replace("\n", "")
		try:
			cur_zipfile.extractall(pwd=str.encode(w))
			print(f"Password: '{w}'")
			exit()
		except:
			pass