#Write a program files-only.py to find only file and not sub directories. Pass directory name as command line argument.


import file1
import os


pname = file1.get_pname()

l1 = os.listdir(pname)
for f in l1:
	if os.path.isfile(f):
		print(f)