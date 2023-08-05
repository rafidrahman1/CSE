from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def plot_symmetric_points(x, y, cx, cy):
    glVertex2f(cx + x, cy + y)
    glVertex2f(cx - x, cy + y)
    glVertex2f(cx + x, cy - y)
    glVertex2f(cx - x, cy - y)
    glVertex2f(cx + y, cy + x)
    glVertex2f(cx - y, cy + x)
    glVertex2f(cx + y, cy - x)
    glVertex2f(cx - y, cy - x)

def midpoint_circle_algorithm(radius, cx, cy):
    x, y = 0, radius
    d = 1 - radius

    glBegin(GL_POINTS)
    while x <= y:
        plot_symmetric_points(x, y, cx, cy)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1

        x += 1
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)

    glPointSize(2.0)
    num_circles = 8
    center_x, center_y = 200, 200  # Adjust the center as needed
    big_circle_radius = 150  # Adjust the radius of the larger circle
    
    for i in range(num_circles):
        angle = (2 * math.pi * i) / num_circles
        offset_x = int(big_circle_radius * math.cos(angle))
        offset_y = int(big_circle_radius * math.sin(angle))
        
        # Calculate the distance between the center of the larger circle and the center of the current smaller circle
        distance = math.sqrt(offset_x ** 2 + offset_y ** 2)
        
        # Adjust the radius of the smaller circles so they touch the center of the larger circle
        small_circle_radius = distance - big_circle_radius
        
        midpoint_circle_algorithm(int(small_circle_radius), center_x + offset_x, center_y + offset_y)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Symmetric Circles")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()