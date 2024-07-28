from math import sqrt
# x²-3x-10 = 0

def segundoGrau(a, b, c):
    delta = b * b - 4 * a * c
    raiz = sqrt(delta)
    x1 = ((b * - 1) + raiz) / 2
    x2 = ((b * - 1) - raiz) / 2
    return print(f'A solução da sua equação é x{x1}. x²{x2}')

segundoGrau(1, -3, -10)
