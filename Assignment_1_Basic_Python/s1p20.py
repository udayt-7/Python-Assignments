#to Take in Two Strings and Display the Larger String without Using Built-in Functions


i = input("Enter the string 1:")
j = input("Enter the string 2:")

c1=0
c2=0

for ch in i:
	c1=c1+1

for ch in j:
	c2=c2+1

if(c1>c2):
	print("String 1 has more characters")
elif(c1 == c2):
	print("Same characters in both strings")
else:
	print("String 2 has more characters")



