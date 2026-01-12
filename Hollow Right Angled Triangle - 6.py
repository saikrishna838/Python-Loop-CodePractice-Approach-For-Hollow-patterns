n = int(input())

for i in range(1, n + 1):
    if i == 1:
        stars = (n - i) + i
        row = "* " * stars 
    elif i == n:
        spaces = (n + i) - 2
        row = " " * spaces + "*"
    else:
        left_spaces = 2 * (i - 1)
        hallow_spaces = (2 * (n - i)) - 2
        row = " " * left_spaces + "* " + " " * hallow_spaces + "*"
    print(row)