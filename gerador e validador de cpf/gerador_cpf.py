from random import randint #importa um gerador de números aleatórios ]. Randint escolhe um número aleatório inteiro dentro dos valores que o usuário escolheu
numero = str(randint(100000000, 999999999)) #nesse caso, irá retornar um número entre 100000000 e 999999999

novo_cpf = numero # elimina os 2 últimos dígitos do cpf
reverso = 10      # contador reverso
soma = 0


for index in range(19):
    if index > 8:   # primeiro índice vai de 0 a 9,
        index -= 9  # são os 9 primeiros digitos do cpf

    soma += int(novo_cpf[index]) * reverso # valor total da multiplicação

    reverso -= 1              #decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (soma % 11)

        if d > 9:             # se o digito for > que 9 o valor é 0
            d = 0
        soma = 0              #zera a soma para a nova contagem
        novo_cpf += str(d)    #concatena o digito gerando o novo cpf
print(novo_cpf)

#não significa que o cpf exista no governo, apenas que é matematicamente válido
