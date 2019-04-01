#to remove given keya = int(input("Enter the range of 1:"))

def a2p7():

	d1 = {}

	a = int(input("Enter the range of dict:"))

	for ch in range(a):
		print("enter key and value:")
		ke1 = (input())
		va1 = (input())

		d1.update({ke1:va1})

	print("Dictionary :",d1)

	a= input("Enter the key to be removed:")

	del d1[a]

	print("after removing:", d1)

a2p7()