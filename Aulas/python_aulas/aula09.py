frase = 'Curso em Vídeo Python'
nova_frase = '   Aprenda Python  '
len = len(frase)
count = frase.count('o')
count_fat = frase.count('o',0,13)
find = frase.find('deo')
encontro = frase.find('Android')
operador = 'Curso' in frase
frase2 = frase.replace('Python','Android')
frase_mai = frase.upper()
frase_min = frase.lower()
frase_cap = frase.capitalize()
frase_title = frase.title()
frase_strip = nova_frase.strip()
frase_rstrip = nova_frase.rstrip()
frase_lstrip = nova_frase.lstrip()
split = frase.split()
juncao = '-'.join(split)
print(frase)
print(frase2)
print(frase_mai)
print(frase_min)
print(len,count,count_fat,find,encontro,operador)
