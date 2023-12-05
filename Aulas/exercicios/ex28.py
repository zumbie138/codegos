from random import randint
numero_maquina = randint(0,5)
numero_humano = int(input('Pensei em um número de 0 a 5, tente adivinhar qual é: '))
if numero_maquina == numero_humano:
    print(f'Você acertou !!, eu pensei no número {numero_maquina}, e você digitou o número {numero_humano} !!')
else:
    print(f'Você errou !!, eu pensei no número {numero_maquina}, e você digitou o número {numero_humano} !!')
    