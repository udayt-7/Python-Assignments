# to find union and intersection of the list



a = int(input("enter the range of list 1: "))
b = int(input("enter the range of list 2: "))

l1 = []
l2 = []
l3 = []

for ch in range(a):
	
	a2 = int(input("enter the list 1: "))
	l1.append(a2)


for ch2 in range(b):
	
	b2 = int(input("enter the list 2: "))
	l2.append(b2)

for ch in l1:
	for ch2 in l2:
		if (ch ==ch2):
			l3.append(ch)


l1.extend(l2)

s1 = set(l1)
l1 = list(s1)

print("Union of the list",s1)
print("Intersection of list:",l3)

