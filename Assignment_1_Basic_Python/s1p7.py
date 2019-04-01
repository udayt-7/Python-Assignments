#smallest divisor of integer



n=int(input("Enter an number:"))
l1=[]
for i in range(2,n+1):
    if(n%i==0):
        l1.append(i)
l1.sort()
print("Smallest divisor:",l1[0])