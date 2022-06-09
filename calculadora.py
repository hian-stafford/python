while True: #enquanto a operação for verdadeira, entrará num laço infinito
    print() #espaço de linha
    num1 = input('Digite um número: ') #pede pro usuário digitar um número
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ') #pede pro usuário digitar um operador
   

    if not num1.isnumeric() or not num2.isnumeric(): #se o que foi digitado não for um número inteiro
        print( 'Voce precisa digitar um numero') #pede pra digitar um número
        continue

    num1 = int(num1) # transforma o que foi digitado (string) em um número (inteiro/int)
    num2 = int(num2) # transforma o que foi digitado (string) em um número (inteiro/int)
    # + - / *
    if operador == '+': #se o operador for '+', faz a soma dos numeros
        print(num1 + num2)
    elif operador == '-': # se o operador for '-', faz a subtração dos numeros
        print(num1 - num2)
    elif operador  == '/': #se for '/', faz divisão do numeros. Dividendo 0 não divide e dá erro (ainda não adicionei algo que mude ou dê uma mensagem de erro)
        print(num1 / num2) 
    elif operador == '*': # se for '*', faz a multiplicação dos numeros
        print (num1 * num2)
    else:
        print('operador inválido') # se digitar algo que não seja um dos operadores acima, mostra essa mensagem na tela

    sair = input('Deseja sair? [s]im ou [n]ão: ') # pergunta se o usuário quer sair
    if sair == 's': # se o usuário digitar 's', sai do laço e finaliza o programa
        break # sai do programa
