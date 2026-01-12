n = int(input())

for i in range(1, n + 1):
    if i == 1:
        spaces = n - i
        row = " " * spaces + "*"
    elif i == n:
        row = "* " * n
    else:
        left_spaces = n - i
        right_spaces = 2 * (i - 2)
        row = " " * left_spaces + "* " + " " * right_spaces + "*"
    print(row)