import os; os.system('cls')
from random import randint
from time import sleep

professor_estudante = input('Você é professor ou estudante: ').capitalize()

questoes = []


if professor_estudante == 'Professor':
    while True:
        criar = int(input('Digite 1 para criar um quiz: '))
        if criar == 1:
            break
    if len(questoes) == 0:
        print('\nNenhuma questão adicionada')
        while True:
            x = []
            print('\nOpções:\n[0] Finalizar\n[1] Adicionar questão\n[2] Editar questão')
            opc = int(input('\nEscolha uma das opções: '))
            if opc == 1:
                x.append(input('\nDigite a questão: '))
                for c in range(1, 5):
                    x.append(input(f'Digite a {c} alternativa: '))
                questoes.append(x)
            elif opc == 2:
                for c in range(len(questoes)):
                    print(f'[{c}] {questoes[c][0]}')
                edit = int(input('\nQual questão você deseja mudar: '))
                x.append(input('\nDigite a nova questão: '))
                for c in range(1, 5):
                    x.append(input('\nDigite a nova alternativa: '))
                questoes[edit] = x
            else:
                break
        print('\nQuiz gerado com sucesso!')
        for l in range(len(questoes)):
            print(f'[{l}] {questoes[l][0]}')
            for c in range(1, 5):
                print(f'{c} - {questoes[l][c]}')

if professor_estudante == 'Estudante':
    quiz = [['1. Qual é o nome do ritmo musical pernambucano que é tradicionalmente tocado durante o carnaval?', 'a) Maracatu', 'b) Samba', 'c) Forró', 'd) Axé'], 
            ['2. Qual é o nome do escritor e dramaturgo pernambucano conhecido pela obra "O Auto da Compadecida"?', 'a) Chico Science', 'b) Luiz Gonzaga', 'c) Ariano Suassuna', 'd) Nena Queiroga'], 
            ['3, Qual é o nome do instrumento musical de percussão típico do maracatu pernambucano?' , 'a) Cuíca', 'b) Tamborim', 'c) Caixa', 'd) Alfaias'], 
            ['4. Qual é o nome do tradicional prato pernambucano feito com feijão-fradinho, camarão seco e outros ingredientes?', 'a) Acarajé', 'b) Bobó de camarão', 'c) Carne de sol', 'd) Feijoada pernambucana'], 
            ['5. Qual é o nome do grande festival de música realizado anualmente em Olinda, Pernambuco?', 'a) Rock in Rio', 'b) Lollapalooza', 'c) Festival de Verão', 'd) Carnaval de Olinda']]
    codigo = randint(100000, 999999)
    print(f'\nPIN: {codigo}')
    while True:
        codigo_aluno = int(input('\nDigite o pin: '))
        if codigo_aluno == codigo:
            break
    nome = input('\nDigite seu nome: ')
    print('\nPersonagens:\n[0] Chico Science\n[1] Luiz Gonzaga\n[2] Ariano Suassuna\n[3] Nena Queiroga\n[4] Capiba')
    while True:
        personagem = int(input('\nEscolha seu personagem: '))
        if personagem >= 0 and personagem <=4:
            break
    while True:
        print('\nVamos começar...')
        boost = 0
        for c in range(3, 0, -1):
            print(f'{c}')
            sleep(1)
        for l in range(5):
            for c in range(5):
                print(f'{quiz[l][c]}')
                if c == 4:
                    resposta = input('\nResposta: ').lower()
                    if l == 0:
                        certa = 'a'
                    elif l == 1:
                        certa = 'c'
                    else:
                        certa = 'd'
                    if resposta == certa:
                        boost+=1
        if boost >= 3:
            print(f'\nParabéns! Você conseguiu salvar o mangue!\nPontuação: {boost}')
            break
        else:
            print(f'Ops! Você não conseguiu salvar o mangue!')
            reiniciar = int(input('\nDigite 1 para reiniciar[0 para sair]: '))
            if reiniciar == 0:
                break
