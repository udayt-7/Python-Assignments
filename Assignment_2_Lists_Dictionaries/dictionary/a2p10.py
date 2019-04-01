
#cipher text translation
		
def a2p10():


	def encrypt1(a,CIPHER_DICT):

		x = CIPHER_DICT.keys()
		nstr = ""

		for c in a:
			if c in x:
				nstr = nstr + CIPHER_DICT.get(c,'NA')
			#print(CIPHER_DICT.get(c,'NA'))
			else:
				nstr = nstr + c

		print(nstr)



	CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f',
 				'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 
 					'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}


	a = input("Enter the term :")


	encrypt1(a,CIPHER_DICT)

a2p10()






	