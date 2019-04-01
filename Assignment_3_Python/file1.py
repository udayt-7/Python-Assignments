#file get, open, read 


import sys
import os

def get_filename():
	if len(sys.argv)>1:
		f_name = sys.argv[1]
		return f_name
	else:
		print("unable to get file")
		sys.exit()

def get_filename2():
	if len(sys.argv)>2:
		pattern = sys.argv[2]
		return pattern
	else:
		print("unable to get pattern/file")
		sys.exit()

def get_pname():
	if len(sys.argv)>1:
		f_name = sys.argv[1]
		return f_name
	else:
		return '.'

def open_file(f_name,mode):
	try:
		r_file = open(f_name,mode)
		return r_file
	except IOError:
		print("File not found", f_name)
		sys.exit()

def file_readline(f_dis):
	while 1:
		line = f_dis.readline()
		if not line:
			break
		else:
			#print(line)
			return

def file_read(f_dis):
	print(f_dis.read())

def file_readlines(f_dis):
	line = f_dis.readlines()
		#print(line)
	return(line)

def testcode():
	f_name = get_filename()
	f_dis = open_file(f_name)
	f_cont =  file_readline(f_dis)
	print(f_cont)	
	file_read(f_dis)
	##file_close(f_dis)
#print("s")
#testcode()

if __name__ == '__main__':
	testcode()