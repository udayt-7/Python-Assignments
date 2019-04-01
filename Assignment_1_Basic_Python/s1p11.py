
# count num of didgits in a number


ch = input("Enter the number:")


c= ch.isdigit()

if (c == True):

 print("num of digits =",len(str(ch)))

else:

 print("NOT A VALID NUMBER")
