distancia = float(input('Informe a distância em km que deseja viajar: '))
if distancia <= 200.0:
    preco = distancia * 0.5
    print(f'Você irá pagar R${preco:.2f} reais por {distancia}km viajados')
else:
    preco = distancia * 0.45
    print(f'Você irá pagar R${preco:.2f} reais por {distancia}km viajados')
    
