from MidPointLine import *
def Reel():
    #Natai body
    x=25
    for i in range(21):
       MidPointLine(40, x, 135, x, 1, 1, 1, 5)
       x+=1
    #Natai border
    MidPointLine(40, 20, 40, 50, 1, 1, 0, 10)
    MidPointLine(20, 35, 40, 35, 1, 1, 0, 10)
    MidPointLine(135, 20, 135, 50, 1, 1, 0, 10)
    MidPointLine(135, 35, 155, 35,  1, 1, 0, 10)
    
    