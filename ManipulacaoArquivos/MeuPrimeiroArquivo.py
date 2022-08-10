# with open("primeiro_arquivo.txt", "a") as arquivo:
#     arquivo.write("\n vamos que vamos!")

# read/r le o conteudo do arquivo
# with open("primeiro_arquivo.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

with open("primeiro_arquivo.txt", "r") as arquivo:
    # readlines le linha a linha
    for linha in arquivo.readlines():
        print(linha)