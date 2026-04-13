a=int(input("Enter a year:"))
result="It is leap year" if (a%4==0 and a%100!=0)or (a%400==0) else "It is not leap year"
print(result)
