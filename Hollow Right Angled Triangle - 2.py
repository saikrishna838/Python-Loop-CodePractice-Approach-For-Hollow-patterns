n = int(input())

for i in range(1, n + 2):
    if i == 1:
        dash = (n - i) + 2
        row = "_" * dash
    else:
        hallow_spaces = (n + 1) - i
        row = "|" + " " * hallow_spaces + "/"
    print(row)
    
    