print('--Calculadora Simples--')
print('-----------------------')

print('1-Adição')
print('2-Subtração')
print('3-Divisão')
print('4-Multiplicação')

op = int(input('Operação: '))
n1 = float(input('N1: '))
n2 = float(input('N2: '))

match op:
    case 1:
            r = n1+n2
            print(f'A soma de {n1} com {n2} é {r:.1f}')
    case 2:
        r = n1-n2
        print(f'A subtração de {n1} com {n2} é {r:.1f}')
    case 3:
        if n2!=0:
           r = n1/n2
           print(f'A divisão de {n1} com {n2} é {r:.1f}')
        else:
            print("Divisão por Zero")
    case 4:
        r = n1*n2
        print(f'A multiplicação de {n1} com {n2} é {r:.1f}')
    case _:
        print('Operação Inválida')

print (f"Resultado: {r:.1f}")





