# sample 1 program 6
# sum of digits


n = int(input("enter number"))
s = 0

while n:
	s += n % 10
	n //= 10
	
print("Sum of digits:",s)



