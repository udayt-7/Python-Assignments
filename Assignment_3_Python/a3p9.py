#Write a program most-recent-file.py to find the most recently modified file in the given directory. 
##The program should accept the directory name as command-line argument and print path to the file 
###(not just filename) that is most recently modified file.


import file1
import os


pname = file1.get_pname()

l1 = os.listdir(pname)

t = 0

for f in l1:
	if os.path.isfile(f):
		if t<os.path.getmtime(f):
			t = os.path.getmtime(f)
			max1 = f

print(os.path.realpath(max1))

