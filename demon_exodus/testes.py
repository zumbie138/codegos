from random import randint
from time import sleep
inventario = {}
while True:
    espolios = {'pelo de rato':20,'anel quebrado':1,'restos de comida':10,'queijo':15}
    for loot , porcentagem in espolios.items():
        porcentagem_definida = randint(0,100)
        if porcentagem_definida <= porcentagem:
            inventario[loot] = inventario.get(loot, 0)+1
    sleep(1)
    print(inventario)