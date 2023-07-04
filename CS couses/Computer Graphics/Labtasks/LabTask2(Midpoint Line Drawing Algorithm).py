from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
import matplotlib.pyplot as plt

def plot_point(x, y):
    plt.scatter(x, y, color='black')

def midpoint_line_algorithm(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        plot_point(x0, y0)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    plot_point(x0, y0)

# Drawing the number 2
midpoint_line_algorithm(5, 10, 10, 10)
midpoint_line_algorithm(10, 10, 10, 15)
midpoint_line_algorithm(10, 15, 5, 15)
midpoint_line_algorithm(5, 15, 5, 5)
midpoint_line_algorithm(5, 5, 10, 5)

plt.axis('scaled')
plt.show()