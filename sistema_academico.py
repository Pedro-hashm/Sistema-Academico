alunos = []
aluno = {}
conf = 's'
contador_nota = 1
media = 0
carga_horaria = int(input('Qual a carga horária em quantidade de aulas da disciplina?: '))
cont = 1
conf2 = int()
from time import sleep

while conf == 's' or conf == 'S':
    contador_nota = 1
    aluno['nome'] = str(input('Nome do aluno: '))
    # Setar a confirmação e o contador de notas + adicionar o nome

    while True:
        nota = float(input(f'Adicione a {contador_nota}º nota: '))
        contador_nota += 1
        media += nota
        if contador_nota >= 3:
            break

    media = media/2
    aluno['media'] = media

    aluno['frequencia'] = int(input('Qual a frequencia do(a) aluno(a): '))

    if aluno['frequencia'] < carga_horaria * 0.75:
        aluno['status'] = 'Reprovado por Falta'
    elif media < 7.0:
        aluno['status'] = 'Reprovado por Nota'
    else:
        aluno['status'] = 'Aprovado'

    alunos.append(aluno.copy())
    aluno.clear()
    media = 0
    # Acrescentar a lista, e resetar o dicionario

    conf = str(input('Quer continuar? [S/N]: '))

    if conf == 'n' or conf == 'N':
        break

sleep(0.5)
print('1 - Editar informações de nome de alunos')
sleep(0.5)
print('2 - Remover aluno existente')
sleep(0.5)
print('3 - Imprimir relatório geral de situação dos alunos')
sleep(0.5)
print('4 - Imprimir relatório de alunos em situação especifica')
sleep(0.5)
print('5 - Encerrar o Programa')
sleep(0.5)

conf2 = int(input('O que você quer fazer? [1~5]: '))

while conf2 != 5:

    if conf2 == 1:
        alt = str(input('Qual o nome do aluno que você quer alterar?: '))
        for aluno in alunos:
            if aluno["nome"] == alt:
                alt = str(input('Digite o novo nome do aluno: '))
                aluno["nome"] = alt

    if conf2 == 2:
        rem = str(input('Qual o nome do aluno que você quer remover?: '))
        for aluno in alunos:
            if aluno["nome"] == rem:
                alunos.remove(aluno)

    if conf2 == 3:
        print('-=-' * 5, 'Relatório Geral', '-=-' * 5)
        sleep(0.5)
        for aluno in alunos:
            print(f'{cont}. {aluno["nome"]} - nota: {aluno["media"]} / {aluno["frequencia"]} - ({aluno["status"]})')
            sleep(0.5)
            cont += 1
        print('-=-' * 17)
        cont = 1

    if conf2 == 4:
        sleep(0.5)
        print('1 - Alunos Aprovados')
        sleep(0.5)
        print('2 - Alunos Reprovados por nota')
        sleep(0.5)
        print('3 - Alunos Reprovados por falta')
        sleep(0.5)
        filtro = int(input('Você quer filtrar por qual situação? [1~3]: '))
        if filtro == 1:
            print('-=-' * 5, 'Relatório Aprovados', '-=-' * 5)
            sleep(0.5)
            for aluno in alunos:
                if aluno["status"] == 'Aprovado':
                    print(f'{cont}. {aluno["nome"]} - nota: {aluno["media"]} / {aluno["frequencia"]} - ({aluno["status"]})')
                    sleep(0.5)
            print('-=-' * 17)
            cont = 1
        if filtro == 2:
            print('-=-' * 5, 'Relatório Reprovados por Nota', '-=-' * 5)
            sleep(0.5)
            for aluno in alunos:
                if aluno["status"] == 'Reprovado por Nota':
                    print(f'{cont}. {aluno["nome"]} - nota: {aluno["media"]} / {aluno["frequencia"]} - ({aluno["status"]})')
                    sleep(0.5)
            print('-=-' * 25)
            cont = 1
        if filtro == 3:
            print('-=-' * 5, 'Relatório Reprovados por Falta', '-=-' * 5)
            sleep(0.5)
            for aluno in alunos:
                if aluno["status"] == 'Reprovado por Falta':
                    print(f'{cont}. {aluno["nome"]} - nota: {aluno["media"]} / {aluno["frequencia"]} - ({aluno["status"]})')
                    sleep(0.5)
            print('-=-' * 25)
            cont = 1

    print('1 - Editar informações de nome de alunos')
    sleep(0.5)
    print('2 - Remover aluno existente')
    sleep(0.5)
    print('3 - Imprimir relatório geral de situação dos alunos')
    sleep(0.5)
    print('4 - Imprimir relatório de alunos em situação especifica')
    sleep(0.5)
    print('5 - Encerrar o Programa')
    sleep(0.5)
    conf2 = int(input('O que você quer fazer? [1~5]: '))



