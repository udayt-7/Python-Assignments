
################################################################################################

									#SAMPLE 2  ASSERTIONS
                          
################################################################################################


################################################################################################

                                             #LISTS

################################################################################################

#_____________________________________________________________________

#1. Python Program to Find the Largest Number in a List

def l_largest_num(li):
	
	return(max(li))
#_____________________________________________________________________

#2. Python Program to Find the Second Largest Number in a List

def l_second_largest(li):

	li =sorted(li)
	return((li[-2]))
#______________________________________________________________________

#3. Python Program to Put Even and Odd elements in a List into Two Different Lists.

def l_odd_even(li):
	l1 = []
	l2 = []
	li = sorted(li)
	for i in li:
		if i%2==0:
			l1.append(i)
		else:
			l2.append(i)
	return(l1,l2)		
#_____________________________________________________________________

#4. Python Program to check whether two lists are same.

def l_same(l1,l2):
	return l1 == l2
#_____________________________________________________________________

#5. Python Program to Find the Union of Lists.

def l_union(l1,l2):
	s = list()
	s = l1+l2
	return s
#_____________________________________________________________________

#6. Python Program to Find the Intersection of Lists.

def l_intersection(l1,l2):
	s= list()
	for ch1 in l1:
		for ch2 in l2:
			if ch1 == ch2:
				s.append(ch1)
	return s
#_____________________________________________________________________

#7. Python Program to find union and intersection of lists without repetition.

def l_intersection2(l1,l2):
	
	s2 = []
	for ch1 in l1:
		if ch1 in l2:
			s2.append(ch1)

	l1.extend(l2)
	s1 = set(l1)
	l1 = list(s1)
	return(l1,s2)

#_____________________________________________________________________

#8. Python Program to Create a List of Tuples with the First Element as the Number 
    #and Second Element as the Square of the Number.

def l_tuple(l1):
	l = [(ch,ch*ch) for ch in l1]
	return l 

#_____________________________________________________________________

#9. Python Program to Remove the Duplicate Items from a List.

def l_dupl(l1):
	s1 = set(l1) 
	l1 = list(s1)
	return l1

#_____________________________________________________________________

#10. Python Program to Read a List of Words and Return the Length of the Longest One.

def l_longest(l1):
	
	max1=len(l1[0])
	for i in range(len(l1)):
		if len(l1[i])>max1:
			max1=len(l1[i])
	return max1
	
#_____________________________________________________________________

##########################################################################################################

                                                #DICTIONARY

##########################################################################################################

#_____________________________________________________________________

#1.	Python Program to Add a Key-Value Pair to the Dictionary

def d_kv():
	
	d1=dict()
	
	for i in range(1,5):	
		d1[i]=i**2
	return d1

#_____________________________________________________________________

#2.	Python Program to Concatenate Two Dictionaries Into One

def d_concate():
	
	d1=dict(r1="uday", r2="dhee", r3="diva")
	d2=dict(r4="tej",r5="pruthv", r6="ash")
	d2.update(d1)
	return d2

#_____________________________________________________________________

#3.	Python Program to Check if a Given Key Exists in a Dictionary or Not

def d_exists(key1):
	d1 = dict(r1="uday", r2="dhee", r3="diva", r4="tej",r5="pruthv", r6="ash")
	return (key1 in d1)
	
#_____________________________________________________________________

#4.	Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def d_xsquare():
	
	d1=dict()
	
	for i in range(1,5):	
		d1[i]=i**2
	return d1


#_____________________________________________________________________

#5.	Python Program to Sum All the Items in a Dictionary

def d_sum1(d1):
	
	return sum(d1.values())

#_____________________________________________________________________

#6.	Python Program to Multiply All the Items in a Dictionary

def d_multiply(d):
	mul=1	
	for ch in d.values():
		mul=mul*ch
	return mul

#_____________________________________________________________________

#7.	Python Program to Remove the Given Key from a Dictionary


def d_remove1(d1,a):
	del d1[a]
	return d1

#_____________________________________________________________________

#8.	Write a function is_empty(my_dict) that takes a dictionary my_dict and 
#   returns True if my_dict is empty and False otherwise.


def d_empty(d1):

	if len(d1):
		return "false"
	else:
		return "true"
		
#_____________________________________________________________________

#9.	Write a function make_dict(key_value_list) that takes a list of tuples key_value_list 
#   where each tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values.

def d_tuple2(l1,l2):
	
	tu = list(zip(l1,l2))
	d1 = dict(tu)
	return d1
	
#_____________________________________________________________________

#10.A simple substitution cipher is an encryption scheme where each letter in an alphabet to replaced by 
# a different letter in the same alphabet with the restriction that each letter's replacement is unique. 
# The template for this question contains an example of a substitution cipher represented a dictionary
# CIPHER_DICTIONARY. 
# Your task is to write a function encrypt(phrase,cipher_dict) that takes a string phrase and 
# # a dictionary cipher_dict and returns the results of replacing each character in phrase by 
# its corresponding value in cipher_dict.

#		CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 
#						'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 
#						'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
#	encrypt("cat", CIPHER_DICT) should return km


def d_cipher(a):
	
	nstr = ""
	

	CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm',
					 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 
					'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 
					'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
	x = CIPHER_DICT.keys()
	for c in a:
		if c in x:
			nstr = nstr + CIPHER_DICT.get(c,'NA')
		
		else:
			nstr = nstr + c
	return nstr

#_____________________________________________________________________

#11.	Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns 
#		a randomly-generated cipher dictionary for the characters in alphabet . You should use the shuffle() method
#		in the random module to ensure that your returned cipher dictionary is random.

import random

def d_shuffle(str1):

	l1 = []
	d1 = {}
	text = "abcdefghijklmnopqrstuvwxyz"
	l1 =list(text)
	random.shuffle(l1)
	c = len(str1)
	p = 0

	for i in str1:
		if c>0:
			d1.update({i:l1[p]})

			p = p + 1
			c = c - 1

	return(len(d1))

#_____________________________________________________________________

#12.	Write a python code to generate grade using dictionary. Dictionary should have student names as keys
# 		(assuming names are unique) and subject_name and mark as value. There are 5 subjects for each student.
# 		Marks should be converted to grades (90 – 100 A+, 80-89 A etc).

def d_marks3(m):
	if 90<=m<=100:
		return 'A+'
	elif 80<=m<=89:
		return 'A'
	elif 70<=m<=79:
		return 'B+' 	
	elif 60<=m<=69:
		return 'B'
	elif 50<=m<=59:
		return 'C+'
	elif 40<=m<=49:
		return 'C'
	elif m<39:
		return 'D'


def d_marks2(x):
	for i in x.keys():
		x.update({i:d_marks3(x[i])})	
	return x
	
def d_marks1(d1):
	d={}
	for i in d1.keys():
		d.update({i:d_marks2(d1[i])})
	return d



#_____________________________________________________________________
