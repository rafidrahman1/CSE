from MidPointLine import *


def Kite():
    a=82
    b=60
    c=90
    
    for x in range(4):
        MidPointLine(a, b, c, b, 0, 0, 1, 5)
        a+=1
        b+=1
        c-=1
    for x in range(16):
        MidPointLine(a, b, c, b, 0, 0, 1, 5)
        a+=1
        b+=1
        c-=1    
    for x in range(17):
        MidPointLine(a, b, c, b, 0, 0, 1, 5)
        a-=1
        b+=1
        c+=1  