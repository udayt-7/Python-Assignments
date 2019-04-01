#s1p24 Cumulative sum of a list [1, 2, 4, …] is defined as  [1, 3, 7, . . .] Writh function cumulative_sum() 


def cumulative_sum (l1):
	
	#l2=[sum(l1[0:x+1]) for x in range(0,len(l1))]
	l2=[]
	new = 0	
	for x in l1:
		new = new + x
		l2.append(new)
	
	print("The new list is: ",l2)

l1=[]

n= int(input("Enter the number of elements in list:"))

for x in range(n):
    element=int(input("Enter elements:"))
    l1.append(element)
print("The original list is:",l1)

cumulative_sum (l1)


