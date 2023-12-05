from random import randint
print('#'*36)
print('########### JO - KEN - PO ##########')
print('#'*36)
placar_h=0
placar_m=0
while True:
    print(f'PLACAR:\nhumano: {placar_h} || maquina: {placar_m}')
    stat=('\033[33mEMPATADO!\033[m','\033[32mVOCÊ VENCEU!\033[m','\033[31mVOCÊ PERDEU!\033[m')
    map = {'1':'\033[1;36mTESOURA\033[m',
           '2':'\033[1mPEDRA\033[m',
           '3':'\033[1;33mPAPEL\033[m'}
    maquina = map[str(randint(1,3))]
    escolha = str(input(f'Escolha entre {map["2"]}, {map["3"]} e {map["1"]}\n1 - {map["1"]}\n2 - {map["2"]}\n3 - {map["3"]}\n4 - Sair.\nEscolha uma das opções: '))
    if escolha == '4':
        break
    humano = map[escolha]
    if maquina == map['1']:
        if humano == map['1']:
            status = stat[0]
        elif humano == map['2']:
            status = stat[1]
            placar_h+=1
        elif humano == map['3']:
            status = stat[2]
            placar_m+=1
    elif maquina == map['2']:
        if humano == map['1']:
            status = stat[2]
            placar_m+=1
        elif humano == map['2']:
            status = stat[0]
        elif humano == map['3']:
            status = stat[1]
            placar_h+=1
    elif maquina == map['3']:
        if humano == map['1']:
            status = stat[1]
            placar_h+=1
        elif humano == map['2']:
            status = stat[2]
            placar_m+=1
        elif humano == map['3']:
            status = stat[0]
    print(f'computador: {maquina} x {humano} :humano\n{status}')
    