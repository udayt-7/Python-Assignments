#palindrome



i = int(input("Enter a number:"))

i1=i
j=0

while(i!=0):
	k = i%10
	j = (j*10)+k
	i = int(i/10)

if (j == i1):
	print("Its a Palindrome")

else:
	print("Not a  Palindrome")




