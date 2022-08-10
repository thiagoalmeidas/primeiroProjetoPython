basedados = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados)

print(float(basedados[0][1]) + float(basedados[1][0]))
