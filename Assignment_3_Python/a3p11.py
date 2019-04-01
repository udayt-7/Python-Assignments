#Write a program find-matching-files.py to find files recursively in a directory tree matching given wildcard pattern. 
##The program should accept the directory and the pattern as command-line argument.


import file1
import os

d_name = file1.get_filename()
pattern = file1.get_filename2()


for f in os.listdir(d_name):
    if f.startswith(pattern) or f.endswith(pattern):
        print(os.path.join(d_name, f))
