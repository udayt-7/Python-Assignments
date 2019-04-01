
import a2p1

################################################################################################

                                             #LISTS

################################################################################################

#_____________________________________________________________________

#1. Python Program to Find the Largest Number in a List

assert(a2p1.l_largest_num([1,2,9,3,7,5,6]) == 9)

#_____________________________________________________________________

#2. Python Program to Find the Second Largest Number in a List

assert(a2p1.l_second_largest([1,2,9,3,7,5,6]) == 7)

#_____________________________________________________________________

#3. Python Program to Put Even and Odd elements in a List into Two Different Lists.

assert(a2p1.l_odd_even([1,2,9,3,7,5,6]) == ([2,6],[1,3,5,7,9]))

#_____________________________________________________________________

#4. Python Program to check whether two lists are same.

assert(a2p1.l_same([1,2,9,3],[1,2,9,3]) == True)

#_____________________________________________________________________

#5. Python Program to Find the Union of Lists.

assert(a2p1.l_union([1,2,9,3],[8,7,5,6]) == [1,2,9,3,8,7,5,6])

#_____________________________________________________________________

#6. Python Program to Find the Intersection of Lists.

assert(a2p1.l_intersection([1,2,9,3],[9,3,5,6]) == [9,3])

#_____________________________________________________________________

#7. Python Program to find union and intersection of lists without repetition.

assert(a2p1.l_intersection2([1,2,9,3],[9,3,5,6]) == ([1,2,3,5,6,9],[9,3]))


#_____________________________________________________________________

#8. Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.

assert(a2p1.l_tuple([1,2,3,4]) == ([(1,1),(2,4),(3,9),(4,16)]))

#_____________________________________________________________________

#9. Python Program to Remove the Duplicate Items from a List.

assert(a2p1.l_dupl([1,1,2,3,3,9,5,6]) == [1,2,3,5,6,9])

#_____________________________________________________________________

#10. Python Program to Read a List of Words and Return the Length of the Longest One.

assert(a2p1.l_longest(['uday', 'dheemanth','divakar','thejas']) == 9)

#_____________________________________________________________________


##########################################################################################################

                                                #DICTIONARY

##########################################################################################################

#_____________________________________________________________________

#1.	Python Program to Add a Key-Value Pair to the Dictionary

assert(a2p1.d_kv()=={1:1,2:4,3:9,4:16})

#_____________________________________________________________________

#2.	Python Program to Concatenate Two Dictionaries Into One

assert(a2p1.d_concate()== {'r1':"uday", 'r2':'dhee', 'r3':'diva', 'r4':'tej','r5':'pruthv','r6':'ash'})

#_____________________________________________________________________

#3.	Python Program to Check if a Given Key Exists in a Dictionary or Not

assert(a2p1.d_exists('r1') == True)
#_____________________________________________________________________

#4.	Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

assert(a2p1.d_xsquare()=={1:1,2:4,3:9,4:16})

#_____________________________________________________________________

#5.	Python Program to Sum All the Items in a Dictionary

assert(a2p1.d_sum1({1:1,2:4,3:9,4:16})== 30)

#_____________________________________________________________________

#6.	Python Program to Multiply All the Items in a Dictionary

assert(a2p1.d_multiply({1:1,2:4,3:9,4:16})== 576)

#_____________________________________________________________________

#7.	Python Program to Remove the Given Key from a Dictionary

assert(a2p1.d_remove1({'1':'1','2':'4','3':'9','4':'16'},'2')== {'1':'1','3':'9','4':'16'})
assert(a2p1.d_remove1({'r1':'uday', 'r2':'dhee', 'r3':'diva'},'r3')== ({'r1':'uday', 'r2':'dhee'}))

#_____________________________________________________________________

#8.	Write a function is_empty(my_dict) that takes a dictionary my_dict and 
#   returns True if my_dict is empty and False otherwise.

assert(a2p1.d_empty({})=="true")
assert(a2p1.d_empty({'r1':'uday'})=="false")

#_____________________________________________________________________

#9.	Write a function make_dict(key_value_list) that takes a list of tuples key_value_list 
#   where each tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values.

assert(a2p1.d_tuple2([1,2,3,4,5],[1,2,3,4,5]) == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5})


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


assert(a2p1.d_cipher("cat") == "km ")
 
#_____________________________________________________________________

#11.	Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns 
#		a randomly-generated cipher dictionary for the characters in alphabet . You should use the shuffle() method
#		in the random module to ensure that your returned cipher dictionary is random.

assert(a2p1.d_shuffle("uday") == (4))


#_____________________________________________________________________

#12.	Write a python code to generate grade using dictionary. Dictionary should have student names as keys
# 		(assuming names are unique) and subject_name and mark as value. There are 5 subjects for each student.
# 		Marks should be converted to grades (90 – 100 A+, 80-89 A etc).


d1={'uday':{'1':91,'2':89,'3':53,'4':8,'5':97},
	'dhee':{'1':91,'2':87,'3':97,'4':8,'5':99},
	'divak':{'1':92,'2':55,'3':57,'4':8,'5':95},
	'tej':{'1':93,'2':82,'3':96,'4':8,'5':91},
	'sri':{'1':97,'2':55,'3':55,'4':8,'5':93}}

assert(a2p1.d_marks1(d1)=={'uday':{'1':'A+','2':'A','3':'C+','4':'D','5':'A+'},
						'dhee':{'1':'A+','2':'A','3':'A+','4':'D','5':'A+'},
						'divak':{'1':'A+','2':'C+','3':'C+','4':'D','5':'A+'},
						'tej':{'1':'A+','2':'A','3':'A+','4':'D','5':'A+'},
						'sri':{'1':'A+','2':'C+','3':'C+','4':'D','5':'A+'}})

#___________________________________________________________________