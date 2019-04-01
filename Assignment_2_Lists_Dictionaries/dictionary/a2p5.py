#to find sum of values

def a2p5():

	a = int(input("Enter the range of 1:"))


	d1 = {}


	for ch in range(a):
		print("enter key and value:")
		ke1 = int(input())
		va1 = int(input())

		d1.update({ke1:va1})

	a = sum(d1.values())

	print("Sum of vales:", a)

a2p5()