from MidPointCircle import*

def Sun(x):
    p=4
    l=8
    MidpointCircle(9, 160, 160,1,0,0,p)
    while l>=0:
     MidpointCircle(l, 160, 160,1,1,0,p)
     l-=1
         
    MidpointCircle(x+1, 160, 160,1,0,0,p)
    # for y in range(j):
    #     MidpointCircle(x+2, 160, 160,1,0,0)    
        
