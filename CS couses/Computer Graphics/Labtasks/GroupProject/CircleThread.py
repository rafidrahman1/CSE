from MidPointCircle import *
from MidPointLine import *

def CircleThread(x):
    if x==1:
       ran=37
    elif x==2:
       ran=32  
    elif x==3:
       ran=27
    elif x==4:
       ran=22  
    elif x==5:
       ran=17    
    elif x==6:
       ran=12  
    elif x==7:
       ran=7
    elif x==8:
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

