#to remove duplicates in list



a = int(input("enter the range of list 1: "))

l1 = []

for ch in range(a):
	
	a2 = int(input("enter the list 1: "))
	l1.append(a2)

s1 = set(l1)
l1 = list(s1)

print("List after removing duplicates", l1)


