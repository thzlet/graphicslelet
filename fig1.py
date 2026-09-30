from OpenGL.GL import *
from OpenGL.GLUT import *

# vértices  (coordenadas de -1 a +1)
A = (-0.9, -0.8)   # esquerda
B = ( 0.9, -0.8)   # direita
C = ( 0.0,  0.8)   # topo


def meio(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


def mistura(cor, k, alvo=(1, 1, 1)):
    """Mistura a cor com 'alvo' (branco = clarear, preto = escurecer)."""
    return tuple(c * (1 - k) + a * k for c, a in zip(cor, alvo))


def tri(a, b, c, cor):
    glColor3f(*cor)
    glVertex2f(*a)
    glVertex2f(*b)
    glVertex2f(*c)


def canto(a, b, c, cor):
    """Subdivide um triângulo (a=esq, b=dir, c=topo) em 4, com variações de tom."""
    ab, bc, ca = meio(a, b), meio(b, c), meio(c, a)
    tri(a, ab, ca, cor)
    tri(ab, b, bc, mistura(cor, 0.15, (0, 0, 0)))
    tri(ca, bc, c, mistura(cor, 0.30))
    tri(ab, bc, ca, mistura(cor, 0.70)) # triângulo invertido do meio


def renderiza():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    AB, BC, CA = meio(A, B), meio(B, C), meio(C, A)

    glBegin(GL_TRIANGLES)
    canto(A, AB, CA, (0.98, 0.55, 0.05)) # canto esquerdo: laranja
    canto(AB, B, BC, (0.10, 0.55, 0.65)) # canto direito: azul petróleo
    canto(CA, BC, C, (0.50, 0.95, 0.30)) # canto de cima: verde
    tri(AB, BC, CA, (0.94, 0.92, 0.88))  # meio: creme
    glEnd()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Fig 1 - Triangulos")
    glutDisplayFunc(renderiza)
    glutMainLoop()


main()
