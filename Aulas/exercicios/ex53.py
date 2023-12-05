texto = str(input('Digite um texto: '))
text_format=texto.strip().lower().replace(' ','')
texto_inv = text_format[::-1]
if text_format == texto_inv:
    print(f'A frase:\n{texto}\n\033[33mPalíndrono:\n{text_format} = {texto_inv}\033[m\n\033[32mÉ um palíndromo!\033[m')
else:
    print(f'A frase:\n{texto}\n\033[33mPalíndrono:\n{text_format} = {texto_inv}\033[m\n\033[31mNÃO É um palíndromo!\033[m')
    