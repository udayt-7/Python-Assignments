#to Calculate the Number of Upper Case Letters and Lower Case Letters in a String


i = input("Enter the string:")
c1=0
c2=0


for ch in i:

	if (ch.isupper()):
		c1+=1
		

	if (ch.islower()):
		c2+=1
		

print("Uppercase: ",c1)
print("Lowercase: ",c2)