a=int(input("Enter you salary per annum"))
if a<250000:
   print("no tax")
elif a>250000 and a<500000:
   print("The tax amount is (5%):",(5/100)*a);
elif a>500000 and a<1000000:
   print("The tax amount is (10%):",(10/100)*a);
elif a>1000000:
   print("The tax amount is (15%):",(15/100)*a);
