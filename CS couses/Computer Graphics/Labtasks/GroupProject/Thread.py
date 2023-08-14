from MidPointCircle import *
from MidPointLine import *

def Thread(x):
    if x==1:
       suta=2
    elif x==2:
       suta=3
    elif x==3:
       suta=4
    elif x==4:
       suta=5
    elif x==5:
       suta=6
    elif x==6:
       suta=7
    elif x==7:
       suta=9    
    elif x==8:
       suta=9 
    else: 
        suta=0    
  
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
       