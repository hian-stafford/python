'''expressoes lambda anonima'''

# def funcao(arg, arg2):
#     return arg * arg2
# var = funcao(2, 2)
# a = lambda x, y: x * y
# print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


"""lista.sort(key=lambda item: item[1])"""

###### OU ######

print(sorted(lista, key=lambda i: i[0]))
print(sorted(lista, key=lambda i: i[1]))

