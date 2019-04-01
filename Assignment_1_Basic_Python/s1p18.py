#to Replace all Occurrences of ‘space’ with 'hyphen' in a String.

i = input("Enter the String: ")

j =""

for ch in i:
	if ch== ' ':
	  j +='-'

	else:
	  j += ch


print(j)