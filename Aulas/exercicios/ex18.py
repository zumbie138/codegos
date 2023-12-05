from math import sin,cos,tan, radians
angulo = float(input('Informe um ângulo: '))
radiano=radians(angulo)
print(f'De {radiano}° temos:\nSeno: {sin(radiano):.4f}\nCosseno: {cos(radiano):.4f}\nTangente: {tan(radiano):.4f}')