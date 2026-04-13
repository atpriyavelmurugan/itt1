l1=list(eval(input("Enter a list:")))
l2=list(eval(input("Enter a list:")))
l3=int("".join(map(str,l1[::-1])))
l4=int("".join(map(str,l2[::-1])))
total=l3+l4
result = [int(x) for x in str(total)][::-1]
print(result)
