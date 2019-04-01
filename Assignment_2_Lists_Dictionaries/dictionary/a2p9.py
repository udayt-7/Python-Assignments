#make_dict(key_value_list) that takes a list of tuples key_value_list where each
##tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values.


def a2p9():

	def make_dict(tu):

		d1 = dict(tu)
		print(d1)

	l1=[]
	l2= []

	a1 = int(input("Enter the no of elements of list 1:"))
	for ch1 in range(a1):
		b1 = input("enter the elements:")
		l1.append(b1)

	a2 = int(input("Enter the no of elements of list 2:"))
	for ch2 in range(a2):
		b2 = input("enter the elements:")
		l2.append(b2)

	tu = list(zip(l1,l2))
	make_dict(tu)

a2p9()