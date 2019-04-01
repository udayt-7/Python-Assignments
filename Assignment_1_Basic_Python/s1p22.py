#to Calculate the Number of Digits and Letters in a String.




i = input("Enter the string:")
c1=0
c2=0


for ch in i:

	if (ch.isalpha()):
		c1+=1
		

	if (ch.isdigit()):
		c2+=1
		

print("Alphabets: ",c1)
print("Digits: ",c2)