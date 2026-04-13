t = int(input("Enter the no.of testcase:"))

for i in range(t):
   x = int(input("Enter thetotal:"))
    s = input().strip()

    chandru_points = 0
    nirmal_points = 0

    for result in s:
        if result == 'C':
            chandru_points += 2
        elif result == 'N':
            nirmal_points += 2
        elif result == 'D':
            chandru_points += 1
            nirmal_points += 1

    if chandru_points > nirmal_points:
        print(60 * x)
    elif nirmal_points > chandru_points:
        print(40 * x)
    else:
        print(55 * x)
