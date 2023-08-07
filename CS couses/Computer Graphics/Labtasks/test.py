import math
r=200
for i in range(8):
        angle = (2*math.pi * i) / 8
        offset_x = int(r * math.cos(angle))/2
        offset_y = int(r * math.sin(angle))/2
        print(offset_x, offset_y)

