n=0
for i in range(1,501):
    if i%2==1:
        if i%3==0:
            n+=i
print(f'A soma de todos os números ímpares que sao múltiplos de três: {n}')