n = int(input())

for i in range(1, n + 1):
    if i == 1:
        ash = (n - i) + 1
        row = "# " * ash
    elif i == n:
        row = "+" 
    else:
        hallow_spaces = 2 * ((n - i) -1)
        row = "+ " + " " * hallow_spaces + "+"
    print(row)