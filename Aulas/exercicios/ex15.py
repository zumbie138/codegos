km = float(input('informe a quantidade de kms que o carro percorreu: '))
d = int(input('informe a quantidade de dias que o carro ficou alugado: '))
preco = d*60 + km*0.15
print(f'Você pagará um total de R${preco:.2f} reais pelo aluguel do carro.')