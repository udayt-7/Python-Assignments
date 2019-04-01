# sample 1 program 9
# reverse number


i = int(input("enter the number"))

reverse =0
while (i > 0):
 r=i%10
 reverse=(reverse*10)+r
 i  //= 10

print(reverse)
