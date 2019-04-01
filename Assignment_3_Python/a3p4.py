#program sumfile.py that takes a filename as argument and prints sum of all numbers in that file. 
#It is assumed that the file will only have one number in every line.


import file1

f_name = file1.get_filename()
f_dis = file1.open_file(f_name,'r')
f = file1.file_readlines(f_dis)

sum1 = 0

for line in f:
	print(line)
	if(line.strip().isdigit()):
		sum1 = sum1 + int(line)
    	
print("sum of integers:",sum1)

