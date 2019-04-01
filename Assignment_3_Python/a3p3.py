#program head.py that takes a filename as command-line argument and prints the first 5 lines of it


import file1

f_name = file1.get_filename()
f_dis = file1.open_file(f_name, 'r')
file1.file_readlines(f_dis)

num_lines = 0

with open(f_name, 'r') as f:
    for line in f:
    	num_lines +=1
    	if(num_lines <= 5):
    		print(line)
