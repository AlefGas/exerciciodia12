lista_idade = []

soma_idade = 0
qtde_menores18 = 0

idade = int(input("Digite a idade do usuario :"))

while (idade > 0):
    lista_idade.append(idade)
    idade = int(input("Digite a idade do usuario:"))

for i in range(len(lista_idade)):
    soma_idade+=lista_idade[i]
    if(lista_idade[i] < 18):
        qtde_menores18+=1
media_idades = soma_idade/ len(lista_idade) #sun(lista_idade / len(lista_idade)

print(f"Media das idades: {media_idades}.2f")
print(f"Quantidade de usuarios menores de 18 anos: {qtde_menores18: .2f}")
