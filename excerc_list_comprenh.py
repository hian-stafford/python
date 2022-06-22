string = '012345678901234567890123456789012345678901234567890123456789' #cris a lista de string

n = 10 #quantidade de vezes que vai pular para o proximo começo
contadores = [i for i in range(0, len(string), n)] # mostra quantas vezes vai pular. Vai pegar de 10 em 10

tuplas = [(i, i + n) for i in range(0, len(string), n)] #gerou as tuplas de inicio e fim (de 0 até 10, 10 a 20 ... 50 a 60)

lista = [string [i:i + n] for i in range(0, len(string), n)] # mostra o resultado dentro da "string" de 0 a 9 para cada volta, até quantas vezes for, pulando de 10 em 10 (parte principal do problema)

linha = [f'string [{i}:{i + n}]' for i in range(0, len(string), n)] #mostra como foi pego os valores da variavel "string" separados do indice 0 ate 10 pulando de 10 em 10

retorno = '.'.join(lista) #pega a lista criada "0123456789" e junta com "." até terminar a contabem



print(f'contadores: {contadores}')
print()
print(f'tuplas: {tuplas}')
print()
print(f'linhas: {linha}')
print()
print(f'lista: {lista}')
print()
print(f'retorno: {retorno}')