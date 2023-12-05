valor = float(input('Informe o valor a pagar: '))
opcao = str(input('Escolha a forma de pagamento:\n1 - À vista dinheiro/cheque.\n2 - À vista no cartão.\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão.\nDigite o número da opção escolhida: '))
if opcao == '1':
    resultado = valor*0.90
    tipo = 'à vista'
elif opcao == '2':
    resultado = valor*0.95
    tipo = 'à vista no cartão'
elif opcao == '3':
    resultado = valor
    tipo = 'em até 2x no cartão'
elif opcao == '4':
    resultado = valor*1.20
    tipo = '3x ou mais no cartão'
else:
    resultado = 0
    print('Opção inválida de pagamento.')
print(f'Você escolheu a opção: \033[1m{tipo}\033[m\nE pagará no total de R${resultado:.2f} reais')