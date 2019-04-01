#to check if given  key exists or not

def a2p3():
	
	a = int(input("Enter the range of 1:"))


	d1 = {}


	for ch in range(a):
		print("enter key and value:")
		ke1 = input()
		va1 = input()

		d1.update({ke1:va1})

	z = d1.keys()
	print("The keys in dictionary:",z)

	b = input("Enter the key to be searched:")

	for c in z:
		if c == b:
			print("Key found")
		
		else:
			pass

	print("key not found")

a2p3()