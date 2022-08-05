# tabuada = int (input("Digite um numero:"))
# print("número digitado é: ", tabuada)
# for valor in range (0,11,1):
#     print (str(tabuada) + "x" + str(valor) + "=" + str((tabuada * valor)))

# numero = int(input("Digite o inicio: " ))
# while numero < 100:
#     print("t" + str(numero))
#     numero += 1
# print("laco encerrado")

# inventario = []
# resposta = "S"
# while resposta == "S":
#     inventario.append(input("Equipamento: "))
#     inventario.append(float(input("Equipamento: ")))
#     resposta = input("Digite S para continuar").upper()
#
# print (inventario)
#
# for elemento in inventario:
#     print(elemento)

# equipamentos, valores, seriais, departamentos = []
# equipamentos = []
# valores = []
# seriais = []
# departamentos = []
# resposta = "S"
# while resposta == "S":
#     equipamentos.append(input("Equipamento: "))
#     valores.append(float(input("Valor: ")))
#     seriais.append(int(input("Número Serial: ")))
#     departamentos.append(input("Departamento: "))
#     resposta = input("Digite \"S\" para continuar: ").upper()
#
# busca=input("\nDigite o nome do equipamento que deseja buscar: ")
# for indice in range(0,len(equipamentos)):
#     if busca == equipamentos[indice]:
#         print("\nEquipamento..: ", (indice+1))
#         print("Nome.........: ", equipamentos[indice])
#         print("Valor........: ", valores[indice])
#         print("Serial.......: ", seriais[indice])
#         print("Departamento.: ", departamentos[indice])

# depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
# for indice in range(0,len(equipamentos)):
#     if depreciacao==equipamentos[indice]:
#         print("Valor antigo: ", valores[indice])
#         valores[indice] = valores[indice] * 0.9
#         print("Novo valor: ", valores[indice])

# serial=int(input("\nDigite o serial do equipamento que será excluido: "))
# for indice in range(0, len(departamentos)):
#     if seriais[indice]==serial:
#         del departamentos[indice]
#         del equipamentos[indice]
#         del seriais[indice]
#         del valores[indice]
#         break
#
# for indice in range(0,len(equipamentos)):
#     print("\nEquipamento..: ", (indice+1))
#     print("Nome.........: ", equipamentos[indice])
#     print("Valor........: ", valores[indice])
#     print("Serial.......: ", seriais[indice])
#     print("Departamento.: ", departamentos[indice])
#
# def preencherInventario(lista):
#     resp="S"
#     while resp == "S":
#         equipamento=[input("Equipamento: "),
#                      float(input("Valor: ")),
#                      int(input("Número Serial: ")), input("Departamento: ")]
#         lista.append(equipamento)
#         resp = input("Digite \"S\" para continuar: ").upper()

usuarios = {}
opcao = input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuário: ").upper()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a última data de acesso: ")
        estacao = input("Qual a última estação acessada: ").upper()
    usuarios[chave] = [nome, data, estacao]

    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar um usuário: ").upper()
print(usuarios)
