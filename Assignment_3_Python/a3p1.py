#program cat.py that takes a filename as command-line argument and prints all the contents of that file.


import file1

f_name = file1.get_filename()

with open(f_name, 'r') as f:
    for line in f:
    	print(line)