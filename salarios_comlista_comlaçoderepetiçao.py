
salarios = [0,0,0,0]
soma = 0

i= 0 #controle do laço do looping

while i < 4:

    salarios[i] = float(input('Salario R$: '))
    soma += salarios[i]
    i += 1

#calcular a media
media = soma/4

print(f'Média Salarial: {media:.2f}')

#imprimir salarios que estao abaixo da média
i = 0

while i<4:
    if salarios[i] < media:
        print(f'Salário abaixo da média: {salarios[i]:.2f}')
        i+=1
        
