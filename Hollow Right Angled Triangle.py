n = int(input())

for i in range(1, n + 1):
    if i == 1:
        spaces = n + i
        row = "* " + " " * spaces  
    elif i == n:
        row = "* " * n
    else:
        hallow_spaces = 2 * (i - 2)
        row =  "* " + " " * hallow_spaces +  "* "
    print(row)