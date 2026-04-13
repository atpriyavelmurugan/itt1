a=int(input("Enter the amount withdraw:"))
b=int(input("Enter the balance amount:"))
if b<500:
   print("not sufficient balance")
else:
   print("you have sufficient balance:")
   if a%100==0:
      print("You are allowed to withdraw")
   else:
      print("Withdraw amount with a multiple of 100")
