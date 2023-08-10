from MidPointCircle import *
from MidPointLine import *

def Thread(x):
    if x==1:
       ran=37
       suta=2
    elif x==2:
       ran=20  
       suta=6
    elif x==3:
       ran=10
       suta=9
    else:
       ran=0
       suta=0   
    
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

   #Ural deya shuta.
    arr=[88, 35, 86, 41, 1, 0, 0, 2]
    for i in range(suta):      
     MidPointLine(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
     arr[0]=86
     arr[1]=arr[3]
     arr[2]=88
     arr[3]+=6
     MidPointLine(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
     arr[0]=88
     arr[1]=arr[3]
     arr[2]=86
     arr[3]+=6
     MidPointLine(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])    