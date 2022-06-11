#codigo que pega um valor e adiciona um aumento de uma certa porcentagem sobre o valor

def percent(n1, n2):  # cria a função percent recebendo 2 parâmetros 
    n2 = n1 * (n2/100)  # n2 recebe o resultado de n1 e adiciona a quantidade de porcentagem escolhida pelo parâmetro que o usuário passou
    return n1 + n2    #retorna a soma entre o número passado em n1 junto com o aumento da porcentagem passado em n2 sobre o valor de n1
    
soma_percentual = percent(50, 10) #passa como parâmetro 50 e 10% para aumentar sobre os 50. 10% de 50 é 5, então a soma sairá 55.0
print(soma_percentual)
# resultado: 55.0

soma_percentual = percent(100, 50)
print(soma_percentual)
soma_percentual = percent(20, 50)
print(soma_percentual)
soma_percentual = percent(15, 100)
print(soma_percentual)
