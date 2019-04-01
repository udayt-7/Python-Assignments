#program grep.py that takes a pattern and a filename as command-line argument 
#and prints all the lines in the file that contain given pattern.

import file1

f_name = file1.get_filename()
pattern = file1.get_filename2()
f_dis = file1.open_file(f_name, 'r')
f = file1.file_readlines(f_dis)

with open(f_name, 'r') as f:
    for line in f:
   		if pattern in line:
   			print("Pattern matched")
   			print(line)

   