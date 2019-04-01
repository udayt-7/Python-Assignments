#to check id dict empty and print


def a2p8():

	def is_empty(d1):

		if bool(d1):
			print("False, Dict:", d1)
		if not bool(d1):
			print("TRUE")


	d1 = {}

	a = int(input("Enter the range of dict:"))

	for ch in range(a):

		print("enter key and value:")
		ke1 = (input())
		va1 = (input())
		d1.update({ke1:va1})


	is_empty(d1)

a2p8()




