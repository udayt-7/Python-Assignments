#to find multiplication of values

def a2p6():

	a = int(input("Enter the range of 1:"))


	d1 = {}


	for ch in range(a):
		print("enter key and value:")
		ke1 = int(input())
		va1 = int(input())

		d1.update({ke1:va1})


	mul =1


	for ch in d1.values():
		mul = mul * ch 

	print("Multplication of vales:", mul)

a2p6()