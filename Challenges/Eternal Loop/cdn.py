# "Eternal Loop" - HTB
# @JhinScripter

import zipfile

cur_file = "37366.zip"

while True:
	try:
		cur_zipfile = zipfile.ZipFile(cur_file, "r")
		next_zipfile = cur_zipfile.namelist()[0]
		cur_zipfile.extractall(pwd=str.encode(next_zipfile.replace(".zip", "")))
		cur_file = next_zipfile
	except:
		print(f"Flag's file: {cur_file}")
		exit()