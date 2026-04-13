a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if (a>b and b>c) or (c>b and b>a):
   print("The second largest is",b)
elif (b>c and c>a) or (a>c and c>b):
     print("The second largest is",c)
else:
   print("The second largest is",a)
