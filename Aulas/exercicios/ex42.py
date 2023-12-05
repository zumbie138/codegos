lado1 = float(input('Coloque o tamano do primeiro lado do triângulo: '))
lado2 = float(input('Coloque o tamano do segundo lado do triângulo: '))
lado3 = float(input('Coloque o tamano do terceiro lado do triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1+lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('O triângulo é \033[31mEQUILÁTERO\033[m.')
    elif lado1 != lado2 != lado3 != lado1:
        print('O triângulo é \033[33mESCALENO\033[m.')
    else:
        print('O triângulo é \033[32mISÓSCELES\033[m.')
else:
    print('\033[1;31mERRO!\033[m\nNão é possivel formar um triângulo com os lados indicados.')