while True:
    #cpf = '16899535009'
    cpf = input('Digite um cpf: ')
    novo_cpf = cpf [:-2]        # elimina os 2 últimos dígitos do cpf
    reverso = 10                 # contador reverso
    soma = 0


    for index in range(19):
        if index > 8:   # primeiro índice vai de 0 a 9,
            index -= 9                                      # são os 9 primeiros digitos do cpf
            soma += int(novo_cpf[index]) * reverso          # valor total da multiplicação

        reverso -= 1                                        #decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (soma % 11)

        if d > 9:                                           # se o digito for > que 9 o valor é 0
            d = 0
            soma = 0                                        #zera a soma para a nova contagem
            novo_cpf += str(d)                              #concatena o digito gerando o novo cpf
print(novo_cpf)

# evita sequencias. EX.: 11111111111, 00000000000...
sequencia = novo_cpf == str(novo_cpf[0] * len(cpf))
if cpf == novo_cpf:                                         #verifica se o novo cpf é igual ao cpf 16899535009
   print('cpf válido')
else:
   print('cpf inválido')
