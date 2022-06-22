l1 = [1,2,3,4,5,6,7,8,9] # cria uma lista
ex1 = [valor for valor in l1] # percorre o valor da lista l1 mostrando todos os valores
#-----------------------------------------------------------------------
ex2 = [v * 2 for v in l1] # multiplica todos os valores de l1 por 2
#-----------------------------------------------------------------------
ex3 = [(v, v2) for v in l1 for v2 in range(4)] #cria uma matriz percorrendo, para cada valor da lista, um numero de 0 a 3
################################################
l2 = ['Mauro', 'Joao', 'Maria'] #lista 2
#-----------------------------------------------------------------------
ex4 = [v.replace('a', '@').upper() for v in l2] #percorre a lista 2 transformando a letra "a" em "@" e colocando tudo maiúsculo
#-----------------------------------------------------------------------
tupla = ( #cria uma tupla
    ('chave', 'valor'), #valores da tupla
    ('chave2', 'valor2'),
)
#-----------------------------------------------------------------------
ex5 = [(y, x) for x, y in tupla] #percorre a tupla criada e verifica x(chave e chave2) e y(valor e valor2), podedno mudar os valores do parenteses para mudar a ordem
ex5 = dict(ex5) #transforma isso num dicionario
###############################################
l3 = list(range(100)) # cria uma lista de 0 a 99

# ex6 = [v for v in l3 if v % 2 == 0]

ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0] #para cada v percorrido dentro da lista, verificar quais numero são divisiveis por 3 ou por 8
#-----------------------------------------------------------------------
ex7 = [v if v % 3 == 0 and v % 8 == 0 else 'x' for v in l3] # se onuemro da lista for divisivel por 3 e por 8, vai mostrar os valores, senão vai mostrar um "x" no lugar dos numeros que nao sao divisiveis



print(ex6) #aqui voce pode mudar e ver cada exemplo