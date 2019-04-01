#to print even no and odd no in two list

a = int(input("enter the range of list: "))

l1 = []
le = []
lo = []


for ch in range(a):
	
	a2 = int(input("enter the list : "))
	l1.append(a2)

for ch in l1:
	if (ch %2 ==0):
		le.append(ch)
	else:
		lo.append(ch)

print("List before sorting: ",l1)
print("Even numbers:", le)
print("Odd numbers:", lo)	