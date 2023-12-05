n1 = float(input('Informe a nota da P1: '))
n2 = float(input('Informe a nota da P2: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'A sua média é: {media:.1f}\n\033[1;31mREPROVADO!!\033[m')
elif 5 <= media <= 6.9:
    print(f'A sua média é: {media:.1f}\n\033[1;33mRECUPERAÇÃO!!\033[m')
elif media >= 7:
    print(f'A sua média é: {media:.1f}\n\033[1;32mAPROVADO!!\033[m')
    
    
    