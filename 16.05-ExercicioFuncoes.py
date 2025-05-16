"""
Escreva um programa em Python que leia n salarios e armazene em uma lista. o Programa deve imprimir a media salarial e os salarios que estiverem abaixo dessa media. Para isso, escreva:
1) Função para obter o numero de salarios
2) Função para criar a lista de salarios
3) Função para calcular a media salarial
4) Funcao para imprimir salarios abaixo da média
5) Função que retorno o maior salário da lista

"""

def qtde_salarios():
    print('*-- Quantidade de Salários --*')
    qtde = int(input('Qtde de salários: '))
    return qtde

def criar_lista(qtde):
    print(f'*-- Criando uma lista com {qtde} Salários --*')
    salarios = []
    i = 0
    while i < qtde:
        salario = float(input('Salário: '))
        salarios.append(salario)
        i+=1
    return salarios    

def media(salarios):
    print('*-- Calcular a média salarial --*')
    soma = 0
    for salario in salarios():
        soma += salario
    media = soma/ len(salarios)
    return media    

def imprimir(salarios, media):
    print('*-- Imprimindo salarios abaixo da média --*')
    for salario in salarios:
        if salario < media:
            print(f'{salario:.2f} abaixo da média')

def maior_salario(salarios):            
    print('*-- Imprimindo maior salário --*')
    maior = 0 
    for salario in salarios():
        if salario > maior:
            maior = salario
    return maior

 #Principal
qtde =  qtde_salarios()
salarios = criar_lista(qtde)
calculo_media = media(salarios)       
imprimir(salarios, media)
print(f'Maior salário: {maior_salario(salarios)}')     

            


