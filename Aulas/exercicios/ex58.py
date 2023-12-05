from random import randint
tentativas = 1
numero_pc = randint(0,10)
print(numero_pc)
numero_humano = int(input('Tente adivinhar que numero eu pensei de 0 a 10: '))
while numero_humano != numero_pc:
    print(f'\033[1,31mERROU!\033[m\nTentativas:{tentativas} !')
    numero_humano = int(input('Tente novamente: '))
    tentativas += 1
print(f'\033[1,32mACERTOU!\033[m\nTentativas:{tentativas} !\n|| Computador: {numero_pc} x {numero_humano} :Humano ||')

    

