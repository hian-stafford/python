def soma (n1, n2):
    return n1 + n2 

def sub (n1, n2):
    n3 = n1 - n2
    return n3

def mult (n1, n2):
    n3 = n1 * n2
    return n3

def div (n1, n2):
    n3 = n1 / n2
    return n3


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('Escolha a operação desejada: ')
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')

escolha = input('Escolha a operação (1, 2, 3, 4): ')


if escolha == '1':
    print(f'{n1} + {n2} = {soma(n1, n2)}')

elif escolha == '2':
    print(f'{n1} - {n2} = {sub(n1, n2)}')

elif escolha == '3':
    print(f'{n1} * {n2} = {mult(n1, n2)}')

elif escolha == '4':
    print(f'{n1} / {n2} = {div(n1, n2)}')

else:
    print('Inválido')
