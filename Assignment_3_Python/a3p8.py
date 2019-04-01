#Write a program largest-file.py to find the largest file in the given directory. 
##The program should accept the directory name as command-line argument and print path to the file (not just filename).


import file1
import os

pname = file1.get_pname()
l1 = os.listdir(pname)

s = 0

for f in l1:
	if os.path.isfile(f):
		if os.path.getsize(f) > s:
			
			s = os.path.getsize(f)
			max1 = f
			
print(max1, s)


