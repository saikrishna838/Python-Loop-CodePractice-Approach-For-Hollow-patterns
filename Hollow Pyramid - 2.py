n = int(input())

for i in range(1, n + 1):
    if i == 1:
        row = str(i)
    else:
        spaces = " " * ((2 * i) - 3)
        row = str(i) + spaces + str(i)
    print(row)
    
for i in range(1, n):
    number = n - i
    if i == (n - 1):
        row = str(1)
    else:
        spaces = " " * (2 * (n - i) - 3)
        row = str(number) + spaces + str(number)
    print(row)