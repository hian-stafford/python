"""FUNÇÕES - DEF EM PYTHON"""

def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    nome = nome.replace('o', '0')
    msg = msg.replace('e', '3')
    msg = msg.replace('o', '0')
    # print(msg, nome)

    return f'{msg} {nome}'

# saudacao()
# saudacao(nome='zezinho', msg='hewllo')
# saudacao('Olá', 'Hian')
# saudacao('Hello', 'Maria')
variavel = saudacao()
print(variavel)