a=int(input("Enter 1st subject mark:"))
b=int(input("Enter 2nd subject mark:"))
c=int(input("Enter 3rd subject mark:"))
f=(a+b+c)/3
if(a>0 and a<100) and (b>0 and b<100) and (c>0 and c<100):
   print("Total marks=",a+b+c)
   print("Average=",f)
else:
   print("Input is not valid")
