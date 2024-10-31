import math


def checar_triangulo(a: int, b: int, c: int):
    lados = [a, b, c]
    lados.sort()
    return lados[0] + lados[1] > lados[2]


def calc_area_triangulo(a: int, b: int, c: int):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print('Informe os lados do triângulo\n')
lado_a = int(input('Informe o primeiro lado: '))
lado_b = int(input('Informe o segundo lado: '))
lado_c = int(input('Informe o terceiro lado: '))

if checar_triangulo(lado_a, lado_b, lado_c):
    print(f'A área do triângulo é: {calc_area_triangulo(lado_a, lado_b, lado_c):.2f}')
else:
    print('Os lados não informam um triângulo')
