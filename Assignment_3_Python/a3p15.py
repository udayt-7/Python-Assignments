#Write a function group(list, size) that take a list and splits into smaller lists of given size.

def group(l1,b):
    
    new = [l1[i:i+b] for i in range(0,len(l1),b)]
    print(new)

a = int(input("enter the range of list 1: "))

l1 = []

for ch in range(a):
	
	a2 = int(input("enter the list 1: "))
	l1.append(a2)

	
b = int(input("enter the size needed to split"))


group(l1,b)