#concat 2 strings

def a2p2():

	a = int(input("Enter the range of 1:"))
	b = int(input("Enter the range of 2:"))

	d1 = {}
	d2 = {}


	for ch in range(a):
		print("enter key and value of dict 1:")
		ke1 = input()
		va1 = input()

		d1.update({ke1:va1})

	for ch in range(b):
		print("enter key and value of dict 2:")
		ke2 = input()
		va2 = input()

		d2.update({ke2:va2})

	d1.update(d2)

	print(d1)
	
a2p2()
