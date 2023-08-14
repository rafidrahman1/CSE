from MidPointLine import *

def NightBackground():
    #Jomin
    y=0
    for i in range(85):
       MidPointLine(0, y, 700, y, 0, 0, 1, 5)
       y+=1
    #Asman  
    for i in range(91):
       MidPointLine(0, y, 700, y, 0, 0, 0, 5)
       y+=1