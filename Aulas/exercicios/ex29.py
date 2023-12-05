from random import randint
velocidade = randint(10,200)
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f'Velocidade excedida, você passou a {velocidade}km/h\nE pagará uma multa de R${multa} reais')
else:
    print(f'Você passou dentro do limite permitido, sua velocidade é: {velocidade}km/h')