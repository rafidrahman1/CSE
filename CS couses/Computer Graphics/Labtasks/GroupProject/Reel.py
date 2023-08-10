from MidPointLine import *
def Reel():
    #Natai border
    MidPointLine(40, 20, 40, 50, 0, 0, 1, 10)
    MidPointLine(20, 35, 40, 35, 0, 0, 1, 10)
    MidPointLine(135, 20, 135, 50, 0, 0, 1, 10)
    MidPointLine(135, 35, 155, 35, 0, 0, 1, 10)
    x=25
    #Natai body
    for i in range(21):
       MidPointLine(40, x, 135, x, 1, 1, 1, 5)
       x+=1