# usuarios = {}
# resp = "S"
# emails = []
# while resp == "S":
#     emails.append(input("Digite um e-mail: ").lower())
#     resp = input("Digite <S> para continuar: ").upper()
#
# tupla = list(enumerate(emails))
# for chave in range(0,len(tupla)):
#     print("Email: ", tupla[chave][1])
#     usuarios[tupla[chave]]=[input("Digite o nome"),
#                             input("Digite o nível")]
#
# for chave,dado in usuarios.items():
#     print("Usuario.:", chave[0])
#     print("Email...: ", chave[1])
#     print("Nome....: ", dado[0])
#     print("Nível...: ", dado[1])

ips={}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo ip ́s: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa=input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1]==pesquisa):
        print(nome)