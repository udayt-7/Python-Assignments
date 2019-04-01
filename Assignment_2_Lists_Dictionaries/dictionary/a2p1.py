#key value pairs in dictionary

def a2p1():

	a = int(input("Enter the range"))
	d = {}

	for ch in range(a):
		print("enter key and value:")
		ke = input()
		va = input()

		d.update({ke:va})

	print(d)

a2p1()