a=int(input("номер столбца1 - "))
b=int(input("номер строки1 - "))
c=int(input("номер столбца2 - "))
d=int(input("номер строки2 - "))

if abs(a - c) == abs(b - d):
    print("YES")
else:
    print("NO")
