#to Replace all Occurrences of ‘a’ with $ in a String.

i = input("Enter the String: ")

j =""

for ch in i:
	if ch== 'a':
	  j +='$'

	else:
	  j += ch


print(j)