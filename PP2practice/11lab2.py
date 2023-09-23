a=int(input("номер столбца1 - "))
b=int(input("номер строки1 - "))
c=int(input("номер столбца2 - "))
d=int(input("номер строки2 - "))
dx = abs(a - c)
dy = abs(b - d)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("YES")
else:
    print("NO")