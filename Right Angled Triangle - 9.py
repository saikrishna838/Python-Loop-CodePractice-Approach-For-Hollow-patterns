n = int(input())

for i in range(1, n + 1):
    if i == 1:
        row = ". " * i
    elif i == n:
        row = ". " * n
    else:
        hallow_spaces = (i - 2)
        row = ". " + "0 " * hallow_spaces + ". "
    print(row)