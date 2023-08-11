from MidPointCircle import *
from MidPointLine import *

def CircleThread(x):
    
    if x=="1":
       ran=37
    elif x=="2":
       ran=20  
    elif x=="3":
       ran=2
    else:
       ran=0
    
    r=11 #radius
    #color
    a=1
    b=0
    c=0
    #centre
    c_x=88
    c_xn=88
    c_y=35    
    for i in range(ran):
      MidpointCircle(r, c_x, c_y,a,b,c)
      c_x+=1
    for i in range(ran):
      MidpointCircle(r, c_xn, c_y,a,b,c)
      c_xn-=1 

