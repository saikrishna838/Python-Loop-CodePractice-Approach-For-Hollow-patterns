m = int(input())
n = int(input())
for i in range(1, m + 1):
    if i == 1 or i == m:
        row = "* " * n
    else:
        zeros = n - 2
        row = "* " + "0 " * zeros + "* "
    print(row)