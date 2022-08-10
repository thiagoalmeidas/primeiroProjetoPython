# dados = list()
# dados.append("Pedro")
# dados.append(25)
# print(dados)

# dados1 = {}
# dados1 = {"nome": "Thiago Almeida", "idade": 20, "sexo": "Masculino"}
# del dados1["sexo"] # deleta da biblioteca
# dados1['peso'] = 95.8 # adiciona na biblioteca
# dados1['nome'] = "Fernando Soares" # altera o dado da biblioteca
# print(f'O {dados1["nome"]} tem {dados1["idade"]} anos')
# for k, v in dados1.items():
#     print(f'{k}: {v}')
#
# brasil = []
# estado1 = {'UF':'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'UF':'Sao Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# for k,v in brasil[0].items():
#     print(f'{k} é {v}')


brasil = list()
estado = dict()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k}:{v}')





