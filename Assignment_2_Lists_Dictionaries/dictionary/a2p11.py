
# random cipher text translation
		
import random

def a2p11():

	dict1 = {}
	text = "abcdefghijklmnopqrstuvwxyz"
	l1 = list(text)
	l2 = []
	
	random.shuffle(l1)

	str1 =input("Enter a string: ")
	
	c = len(str1)
	p = 0

	for i in str1:
		if c>0:
			dict1.update({i:l1[p]})

			p = p + 1
			c = c - 1

	print(dict1)

a2p11()