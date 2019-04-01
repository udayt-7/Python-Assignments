# tuple, element 1 number element 2 its square


a = int(input("enter the range of list 1: "))

l1 = []

for ch in range(a):
	
	a2 = int(input("enter the list 1: "))
	l1.append(a2)
print(l1)

for ch in l1:
	z = (ch, (ch*ch))
	print(z)