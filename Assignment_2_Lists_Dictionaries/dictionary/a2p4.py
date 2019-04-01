#to display numbers a n, n*n...

def a2p4():

	a = int(input("Enter the range of dict:"))


	d1 = {}


	for ch in range(1,a+1):
		d1.update({ch:ch*ch})

	print(d1)
	
a2p4()