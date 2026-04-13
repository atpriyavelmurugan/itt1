t=int(input("Enter the no.of range of testcases:"))
for i in range(t):
   n=int(input("Enter n.of tyres:"))
   if 2<=n and n<=1000:
      if n%4==0:
         print("no")
      elif n%4==2:
         print("yes")
      else:
         print("no")
