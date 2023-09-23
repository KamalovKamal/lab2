#str='some string "some quote"'
#print ('good job')
#print (str)
#print ("adadf")
#str2="hello " "wordl"
#print (str2)
#a= 3.5
#b = int (a)
#c=int (12.9)
#d=int('3')
#e=int('-3')
#print (b,c,d,e)
#f=int ('0b11',2)
#y=int('0o12',base=8) #10 in decimal
#z=int ('0xb',base=16) #10 in decimal
#print (f,y,z)

#str_to_float = '-2500'
#x = float (str_to_float)
#int_to_float =123
#y=float(int_to_float)
#print (x,y)

#complex(real, imag)
#v1 = complex(1,2)
#v2 = complex(5, 2e-2)
#v3 = complex("3+4j")
#print (v1,v2,v3)

#x=int(input("Please insert any integer number: "))
#if( x<0):
#    print("x is less than 0! ")
#elif x == 0:
#    print ("x is zero!")
#elif x==1:
#    print("x is one !")
#else:
#    print ("else statement ")


#a = None 
#if a is None:
#    print ("a is None")
#else:
#    print ("a is not None")
 

#a = 5
#b = 5
#if a<b:
#    res = a+b
#elif a==b:
#    res = a*b
#else:
#    res=a-b
#res=a+b if a<b else a-b 
#res2 = a+b if a<b else (a*b if a==b else a-b)
#print (res,res2)

#count = 3
#while count < 7:
#    print (count, "<7")
#    count = count +1
#else :
#    print (count, "=7")

#while True:
#    print('eternity', end='')

#while 2 < count < 10:
 #    print (count, "<7")
  #   count = count +1

#numbers = ["one","two","three","four"]
#for num in numbers:
#    print(num)

#n=len(numbers)
#for i in range (n):
#    print (numbers[i], end=' ')

#d = {0: 'zero ', 1: 'one', 2: 'two' ,3:'three'}
#for key, value in d.items():
#    print("Key is ", key, "Value is ", value)


for i in range(10):
    if(i==4):
        continue
    print (i,end=' ')
    if(i==6):
        break

print()
for i in range(5,10):
     print (i,end=' ')

print()
for i in range(5,10,3):
    print (i,end=' ')
    
    
