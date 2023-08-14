from MidPointLine import *

def Kite(x):
    if x==1:
       suta=0
       s=0

    elif x==2: 
       suta=15
       s=2

    elif x==3: 
       suta=30
       s=3   

    elif x==4:
       s=4
       suta=40

    elif x==5:
       s=5
       suta=50

    elif x==6:
       s=7
       suta=60         

    elif x==7:
       s=8
       suta=80

    elif x==8:
       s=9
       suta=85

    else: 
       s=0
       suta=0     


    a=76+s
    b=60+suta
    c=96-s

    for x in range(10-s):
        MidPointLine(a, b, c, b, 1, 1, 0, 5)
        a+=1
        b+=1
        c-=1
    for x in range(20-s):
        MidPointLine(a, b, c, b, 1, 1, 0, 5)
        a+=1
        b+=1
        c-=1    
    for x in range(21-s):
        MidPointLine(a, b, c, b, 1, 1, 0, 5)
        a-=1
        b+=1
        c+=1  