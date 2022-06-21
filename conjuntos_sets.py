'''
add (adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas nao em ambos)
'''


# s1 = {1,2,3,4,5,6} #suporta numeros, strings ou tuplas

# for v in s1:
#     print(v)
########################################################
#s1 = set() #set vazio
# s1.add(1) #set com valor
# s1.add(2)
# s1.add(3)
# s1.add(4)

# s1.discard(2) #descarta o set 2

# s1.update('a') #adiciona o 'a'
########################################################

#s1.update('Python') #separa a palavra em ordem aleatória

# print(s1)

########################################################

# l1 = [1,2,3,4,5,6,6,6,6,6,6,6,7,8,9, 'User', 'User'] #dicionario com elementos duplicados
# l1 = set(l1) #remove os elementos duplicados
# l1 = list(l1) #transforma de volta numa lista, podendo ou não estar fora de ordem

# print(l1[-1])
########################################################

# s1 = {1,2,3,4,5,7}
# s2 = {1,2,3,4,5,6}
# # s3 = s1 | s2 #faz a união da lista, iterando todos os elementos
# # s3 = s1 & s2 #pega todos os elementos que estao presentes em ambas os sets
# # s3 = s1 - s2 #mostra o set que está na esquerda (s1), mostrando o unico numero diferente que esta nele
# s3 = s1 ^ s2 #pega os elementos que estao e nao estao ao mesmo tempo no sets
# print(s3)
########################################################

l1 = ['Maria', 'Joao', 'Luiz']
l2 = ['Maria','Maria','Maria','Maria', 'Joao', 'Joao', 'Joao', 'Joao', 'Joao', 'Joao', 'Joao', 'Joao', 'Luiz']

l1 = list(set(l1))
l2 = list(set(l2))

print(l1, l2)