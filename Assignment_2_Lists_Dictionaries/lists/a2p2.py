#to find 2nd largest no in a list



a = int(input("enter the range of list: "))

l1 = []


for ch in range(a):
	
	a2 = int(input("enter the list : "))
	l1.append(a2)

l1= sorted(l1)

print("2nd largest element:" ,l1[-2])

#l1.remove(max(l1))

#l2 = l1

#print("2nd largest element:" ,max(l2))