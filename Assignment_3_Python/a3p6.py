#Write a program copyfile.py to copy one file to another. 
##It should accept two filenames as command-line arguments and copies the first one into the second.


import file1

f_name = file1.get_filename()
file2 = file1.get_filename2()
f_dis = file1.open_file(f_name,'r')
f_dis2 = file1.open_file(file2,'a')


for line in f_dis:
	f_dis2.write(line)


