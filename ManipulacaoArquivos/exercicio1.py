from datetime import datetime
from operator import itemgetter
from random import randint
from time import sleep

# EXERCICIO 90
#
# aluno = dict()
#
# aluno['Nome'] = str(input("Digite o nome: "))
# aluno['Media'] = float(input("Digite a média: "))
#
# approve = True
# if aluno['Media'] <= 5:
#     approve = False
#     aluno['situacao'] = "Reprovado"
# else:
#     aluno['situacao'] = "Aprovado"
#
# print(f'Nome: {aluno["Nome"]} \n'
#       f'Média de {aluno["Nome"]}: {aluno["Media"]} \n'
#       f'Situacao de desempenho: {aluno["situacao"]}' , aluno.items())

# EXERCICIO 91
# jogo = {
#     'jogador1': randint(1, 6),
#     'jogador2': randint(1, 6),
#     'jogador3': randint(1, 6),
#     'jogador4': randint(1, 6)
# }
# raking = list()
# print('Valores Sorteados: ')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1) # timer mostra a cada 1 segundo
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # sorted alinha por ordem
# print('-=' * 20)
# print('-----Ranking dos Jogadores-----')
# for i, v in enumerate(ranking):
# para fazer o for em uma lista se usa o enumerate, itengatter mostra por onde tem que ser a ordem
#     print(f'{i + 1} Lugar: {v[0]} com {v[1]}.')
#     sleep(1)
# print(ranking[0])

# EXERCICIO 92
# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('Carteira de Trabalho: (0 nao tem)'))
# if dados['ctps'] != 0:
#     dados['contratacao'] = int(input('Ano de Contratacao: '))
#     dados['salario'] = int(input('Salario: R$'))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
# print('-=' * 30)
# for k, v in dados.items():
#     print(f' - {k} tem o valor {v}')

# EXERCICO 93
# jogador = {}
# partidas = list()
# jogador['nome'] = str(input('Nome do Jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'   Quantos gols na partida {c + 1}?')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' * 30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i + 1}, fez {v} gols')
# print(f'Foi um total de {jogador["total"]} gols')

# EXERCICO 94
dados = dict()
pessoa = list()

decisao = "S"
soma = media = 0
while decisao == "S":
    dados['nome'] = str(input('Nome: '))

    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in "MF":
            break
        print("Erro!, digite M ou F")

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoa.append(dados)

    while True:
        decisao = str(input("Quer Continuar? [S/N] ")).upper()
        if decisao in "SN":
            break
        print("Erro!, digite S ou N")


print(pessoa)
print('-=' * 30)
print(f'Ao todo temos {len(pessoa)} pessoas cadastradas!')
media = soma / len(pessoa)
print(f'A Média de idade das pessoas é de {media}')


