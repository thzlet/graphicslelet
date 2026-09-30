from OpenGL.GL import *
from OpenGL.GLUT import *

QUADRANTES = [
    # superior esquerdo
    ((-1, 0, 0, 1), [(0.95, 0.65, 0.80), (0.15, 0.30, 0.75), (0.70, 0.70, 0.85), (1.00, 0.85, 0.70)]),
    # superior direito
    ((0, 0, 1, 1),  [(0.93, 0.75, 0.50), (0.95, 0.55, 0.10), (0.70, 0.55, 0.65), (0.88, 0.92, 0.95)]),
    # inferior esquerdo
    ((-1, -1, 0, 0), [(1.00, 1.00, 1.00), (0.75, 0.40, 0.50), (0.55, 0.05, 0.25), (0.98, 0.92, 0.70)]),
    # inferior direito
    ((0, -1, 1, 0), [(0.55, 0.50, 0.80), (1.00, 1.00, 1.00), (1.00, 0.70, 0.85), (0.80, 0.40, 0.85)]),
]


def renderiza():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    for (x0, y0, x1, y1), cores in QUADRANTES:
        cantos = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for cor, (x, y) in zip(cores, cantos):
            glColor3f(*cor) # GPU interpola as cores entre os vértices
            glVertex2f(x, y)
    glEnd()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Figura 3 - Quadrantes")
    glutDisplayFunc(renderiza)
    glutMainLoop()
main(
