perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a' : '1',
            'b' : '4',
            'c' : '22',
            'd' : '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 4*4?',
        'respostas': {
            'a' : '1',
            'b' : '2',
            'c' : '44',
            'd' : '16',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10+2?',
        'respostas': {
            'a' : '20',
            'b' : '4',
            'c' : '12',
            'd' : '5',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 10*2?',
        'respostas': {
            'a' : '12',
            'b' : '20',
            'c' : '22',
            'd' : '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 15+9?',
        'respostas': {
            'a' : '24',
            'b' : '4',
            'c' : '22',
            'd' : '5',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 6': {
        'pergunta': 'Quanto é 5*5?',
        'respostas': {
            'a' : '1',
            'b' : '4',
            'c' : '22',
            'd' : '25',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 7': {
        'pergunta': 'Quanto é 9*9?',
        'respostas': {
            'a' : '81',
            'b' : '4',
            'c' : '22',
            'd' : '5',
        },
        'resposta_certa': 'a',
    },'Pergunta 8': {
        'pergunta': 'Quanto é 10/5?',
        'respostas': {
            'a' : '1',
            'b' : '50',
            'c' : '2',
            'd' : '22',
        },
        'resposta_certa': 'c',
    },'Pergunta 9': {
        'pergunta': 'Quanto é 2*7?',
        'respostas': {
            'a' : '3',
            'b' : '14',
            'c' : '22',
            'd' : '90',
        },
        'resposta_certa': 'b',
    },'Pergunta 10': {
        'pergunta': 'Quanto é 5+8?',
        'respostas': {
            'a' : '13',
            'b' : '4',
            'c' : '22',
            'd' : '5',
        },
        'resposta_certa': 'a',
    },
}

respostas_certas = 0
for pergunta, pergunta_values in perguntas.items():
    print(f'{pergunta}: {pergunta_values["pergunta"]}')

    for resposta, resposta_values in pergunta_values['respostas'].items():
        print(f'[{resposta}]: {resposta_values}')

    resposta_user = input('Resposta: ')

    if resposta_user == pergunta_values['resposta_certa']:
        print('Acertou')
        respostas_certas += 1
    
    else:
        print('Errou')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas. A porcentagem de acerto foi de {porcentagem_acerto}')