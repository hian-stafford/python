# d1 = dict (chave1 = 'Valor da chave', chave2 = 'valor da outra chave')#cria a chave e o valor da chave
# d1 ['nova_chave'] = 'Valor da nova chave' #adiciona uma nova chave no dicionário
# print(d1)


# d1 = {'chave1':'Valor', 'chave1':'Valor', 'chave1':'Valor final da chave'} #por serem a mesma chave, ele considera apenas o valor final

# print(d1)


# d1 = {1: 'Valor1', 2: 'Valor2', 3: 'valor real da nova chave'} #por serem chaves diferentes, os valores são diferentes
# print(d1[1])


# d1 = {
# 'str' : 'valor',
# 123: 'Outro valor',
# (1,2,3,4) : 'Tupla'
# }

# print(d1[(1,2,3,4)])


clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Moreira'
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira',
    },
}

# iteração das listas. Além da lista, irá mostrar a lista dentro da lista.
for clientes_123, clientes_n_s in clientes.items():
    # mostra qual cliente será exibido no laço
    print(f'Exibindo {clientes_123}')
    # laço para ver o nome e o sobrenome da lista, alternando entre eles, o resultado do nome completo dentro da lista clientes_nome_sobrenome (clientes_n_s)
    for dados_n_s, dados_nome_completo in clientes_n_s.items():
        # mostra o nome e depois o sobrenome da lista é igual ao resultado que está pré definido
        print(f'\t{dados_n_s} = {dados_nome_completo}')
