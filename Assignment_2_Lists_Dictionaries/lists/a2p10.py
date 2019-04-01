 #to Read a List of Words and Return the Length of the Longest One.


a = int(input("enter the range of list 1: "))

l1 = []

for ch in range(a):
	
	a2 = input("enter the list 1: ")
	l1.append(a2)

print(max(l1))