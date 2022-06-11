# Desafio FizzBuzz:

- Se o número for divisível por 3, no lugar do número escreva 'Fizz'
- Se o número for divisível por 5, no lugar do número escreva 'Buzz'
- Se o número for divisível por 3 e 5, no lugar do número escreva 'FizzBuzz'
- Se não for múltiplo de nada, retorna o número

```Py
def fizz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0: # Se o número for divisível por 3 e 5, no lugar do número escreva 'FizzBuzz'
        return f'FizzBuzz, {n1} é divisivel por 3 e 5'

    if n1 % 5 == 0: # Se o número for divisível por 5, no lugar do número escreva 'Buzz'
        return f'buzz, {n1} é divisivel por 5'

    if n1 % 3 == 0: # Se o número for divisível por 3, no lugar do número escreva 'Fizz'
        return f'fizz, {n1} é divisivel por 3'

    return n1 # Se não for múltiplo de nenhum dos dois, retorna o próprio número

from random import randint  #importa o randint da biblioteca random para gerar numeros aleatorios que o usuário definir
for i in range(100):  #cria um laço de 0 até 100
    aleatorio = randint(0, 100) #a variavel "aleatorio" recebe a função randint entre 0 e 100 para criar numeros aleatorios nesse intervalo
    print(fizz(aleatorio)) #mostra a mensagem dependendo do numeros gerado aleatoriamente
 ```
