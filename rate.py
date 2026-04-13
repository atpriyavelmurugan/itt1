p=int(input("Enter the principle ampunt:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter the time period:"))
if (p<1 and p>=100000) or (r<1 and r>=20) or (t<1 and t>=10):
   print("Invalid")
else:
   print("simple interest is",(p*r*t)/100)
