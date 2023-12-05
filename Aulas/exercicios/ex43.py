peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso/altura**2
if imc < 18.5:
    print(f'Seu IMC é: \033[33m{imc:.1f}\033[m\nVocê está \033[1;37mabaixo do peso\033[m.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é: \033[33m{imc:.1f}\033[m\nVocê está no \033[1;32mpeso ideal\033[m.')
elif 25 < imc <= 30:
    print(f'Seu IMC é: \033[33m{imc:.1f}\033[m\nVocê está com \033[1;35msobre peso\033[m.')
elif 30 < imc <= 40:
    print(f'Seu IMC é: \033[33m{imc:.1f}\033[m\nVocê está com \033[1;31mobesidade\033[m.')
elif imc > 40:
    print(f'Seu IMC é: \033[33m{imc:.1f}\033[m\nVocê está com \033[7mobesidade morbida\033[m.')