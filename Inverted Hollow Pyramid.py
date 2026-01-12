n = int(input())

for i in range(1, n + 1):
    if i == 1:
        stars = n
        row = "* " * n
    elif i == n:
        spaces = n -1
        row = " " * spaces + "*"
    else:
        left_spaces = i -1
        hallow_spaces = (2 * (n - i)) - 1
        row = " " * left_spaces + "*" + " " * hallow_spaces + "*"
    print(row)