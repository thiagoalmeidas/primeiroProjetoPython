from Dicionarios.Functions import *

usuarios = {}
# opcao = perguntar()
#
#
# while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
#     if opcao == "I":
#         inserir(usuarios)
#     opcao = perguntar()

print(usuarios)

print("Preenchendo")
preencherInventario(usuarios)
print("Exibindo")
exibirInventario(usuarios)
print("Pesquisando")
localizarPorNome(usuarios)
print("Alterando")
depreciarPorNome(usuarios, 20)
print("Excluindo")
print(excluirPorSerial(usuarios))
exibirInventario(usuarios)
print("Resumindo")
resumirValores(usuarios)

