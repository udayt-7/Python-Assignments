#check whether both lists are same


a = int(input("enter the range of list 1: "))
b = int(input("enter the range of list 2: "))

l1 = []
l2 = []



for ch in range(a):
	
	a2 = int(input("enter the list 1: "))
	l1.append(a2)


for ch2 in range(b):
	
	b2 = int(input("enter the list 2: "))
	l2.append(b2)

if l1.sort() == l2.sort():
	print("Both lists or same")
else:
	print("Different lists")


