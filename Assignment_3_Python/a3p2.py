#program wc.py that takes filename as argument and counts number of lines, words and chars in file.


import file1

f_name = file1.get_filename()

num_lines = 0
num_words = 0
num_chars = 0

with open(f_name, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        for ch in line:
        	if(ch != "\n"):
        		num_chars +=1 
print("characters:", num_chars)
print("words:", num_words)
print("lines:", num_lines)
