#Write a program ls.py that takes path to a directory as command-line argument and prints all the files in that directory. 
##When no argument is specified, it should list the files in the current directory.


import file1
import os


pname = file1.get_pname()

l1 = os.listdir(pname)

print(l1)
