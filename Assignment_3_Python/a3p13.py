#Write a function unique to find all the unique elements of a list.


def unique(l1):

	l3 =[]
	for i in range(len(l1)):
		if l1[i] not in l1[i+1:] and l1[i] not in l1[:i] and l1[i] not in l3:
				l3.append(l1[i])
	print(l3)


a = int(input("enter the range of list 1: "))

l1 = []

for ch in range(a):
	
	a2 = int(input("enter the list 1: "))
	l1.append(a2)
	
unique(l1)



