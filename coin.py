t=int(input("Enter no.of testcase:"))
for i in range(t):
   a=int(input("Enter no.of coins:"))
   b=int(input("Enter no.of coins:"))
   c=int(input("Enter no.of coins:"))
   d=int(input("Enter no.of coins:"))
   if a>=0 and a<=1000000:
      if a>b:
        b=b+c
      else:
        a=a+c

      if b>a:
        a=a+d
      else:
        b=b+d

      if a>=b:
        print("N")
      else:
        print("S")
