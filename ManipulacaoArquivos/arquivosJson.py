import json

with open("bd.json", "r") as arquivo:
    dic = json.load(arquivo)
    for chave, dados in dic.item():
        print(chave + "" + str(dados))

