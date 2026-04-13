t=int(input("Enter num of tetscases:"))
for i in range(t):
   n=int(input("Enter the no of rows:"))
   triangle = []
   for i in range(n):
     row = list(map(int, input().split()))
     triangle.append(row)
for row in range(n - 2, -1, -1):
    for col in range(len(triangle[row])):

        l= triangle[row + 1][col]
        r = triangle[row + 1][col + 1]

        triangle[row][col] += max(l, r)
        print(triangle)
