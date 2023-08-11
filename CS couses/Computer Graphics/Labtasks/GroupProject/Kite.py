from MidPointLine import *

def Kite(x):

    if x=="1":
       suta=0
       s=0

    elif x=="2": 
       suta=48
       s=3

    elif x=="3":
       s=7
       suta=83
    else:
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