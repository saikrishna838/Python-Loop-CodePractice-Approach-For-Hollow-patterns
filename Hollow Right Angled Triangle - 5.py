n = int(input())

for i in range(1, n + 1):
    if i == 1:
        spaces = 2 * (n - i)
        row = " " * spaces + "*" * i
    elif i == n:
        row = "* " * n
    else:
        hallow_spaces = 2 * (i - 2)
        left_spaces = 2 * (n - i)
        row = " " * left_spaces + "* " + " " * hallow_spaces + "*"
    print(row)