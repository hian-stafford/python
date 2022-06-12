'''Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range'''


secreto = 'perfume' #palavra secreta definida
digitadas = [] #lista de letras para serem salvas e lidas
chances = 3 #condição para ter apenas 3 chances de tentativa

while True: #laço que testa as chances
    if chances <= 0: #condição pras chances não passarem de 0
        print('Voce perdeu!!!')
        break

    #INICIO do joguinho
    #pergunta ao usuário a letra
    letra = input('Digite uma letra: ')

    #verifica se a letra foi apenas 1
    if len(letra) > 1:
        print('Isso não vale. Digite apenas 1 letra por vez')
        continue

    digitadas.append(letra) #adiciona a letra digitada na variável "digitadas"
    
    #se a letra digitada estiver dentro da variavel "secreto"
    if letra in secreto:
        print(f'Acertou uma das letras "{letra}". Digite a próxima letra')
    #se a letra não estiver na variável "secreto"
    else:
        print(f'Affs, a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop() #se a letra não existe, "pop" vai remover a última letra digitada que não está na palavra secreta

    secreto_temporario = '' #variável vazia para receber a letra temporariamente para guardar até a resposta final

    # nova variavel criada (letra_secreto). Se esta variavel estiver dentro de
    for letra_secreto in secreto: # variável "letra_secreto" percorre as letras dentro de "secreto" verificando a posição
        if letra_secreto in digitadas: # se a "letra_secreto" (última letra que o usuário digitou) estiver em "digitadas",
            secreto_temporario += letra_secreto # o "secreto_temporario" vai ser incrementado da letra que foi digitada em "letra_secreto" 
        else: 
            secreto_temporario += '*' # se a letra não estiver na palavra, troca as letras restantes em "*"


    if secreto_temporario == secreto: # se a palavra completa for igual a palavra definida, o usuário ganha
        print(f'Parabéns, você ganhou!!!! A palavra era {secreto}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}.') # se ainda não for exatamente a palavra igual, mostra como a palavra está com "*"

    if letra not in secreto: #se a letra digitada não estiver dentro da palavra "secreto"
        chances -= 1 #perde uma chance
    print(f'Voce ainda tem {chances} chances.') #mostra quantas chances o usuário ainda tem para concluir a palavra
    print() #oula linha

# l2 = ['string', True, 10, -20.5]

# for elem in l2:
#     print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')


# l2 = list (range(0, 100, 8))

# for valor in l2:
#     print(valor)



# string = 'ABacanaCDE'
# print(string[2])