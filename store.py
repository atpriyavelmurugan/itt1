a=int(input("Enter the purchase amount:"))
b=(20/100) * a
c=(10/100) * a
print("------------------------------")
print("           BILL               ")
print("------------------------------")
print("The actual price is",a)
if a>=5000:
   print("The discount percentage is : 20%")
   print("The bill amount is",b)
elif a>=3000:
   print("The discount percentage is : 10%")
   print("The bill amount is",c)
else:
   print("The discount percentage is : 0%")
   print("no discount")
