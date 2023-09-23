a=int(input())
b=int(input())
c=int(input())
if(a==b==c):
    print ("3")
elif ((a==b or a==c) or (b==a or b==c) or (c==a or c==b)):
    print ("2")
else: print("0")