salarios = []
soma = 0 
400

for i in range (4):
    salario = float(input('Salario R$: '))
    soma += salario
    salarios.append(salario) #adiciona salario em salarios

media = soma/4

for salario in salarios: 
    if salario < media:
        print(f'Salario abaixo da media: {salario:.2f}')