
#Escreva um programa que leia 5 nomes e exiba a quantidade que inicia com vogal

#criando lista vazia
nomes = []
nomes_vogal = []

#preenchendo a lista com nomes
for i in range (5):
    nome = input('Nome: ')
    nomes.append(nome)

#variavel contadora
qtde = 0

#percorrer a lista de nomes, verificando iniciadas com vogal

for nome in nomes:
    if nome [0] == 'A' or nome [0] == 'E' or nome [0] == 'I' or nome [0] == 'O'  or nome [0] == 'U':
        qtde+=1 
        nomes_vogal.append(nome)

print(f'Quantidade: {qtde}')  
print (nomes_vogal)
