listas_palavras_ing = []
listas_palavras_pt = []
resp = 1

while(resp != 0):
    listas_palavras_ing.append(input("Digite uma palavra em ingles:"))
    listas_palavras_pt.append(input("Digite uma palavra em portugues:"))
    resp = int(input("Deseja continuar (1-sim/0-nao?"))

palavra = input("Digite a palavra em ingles para ser traduzida: ")

if(palavra in listas_palavras_ing):
    pos_palavra = listas_palavras_ing.index(palavra)
    print(f"a palavra em portuhgues eh {listas_palavras_pt[pos_palavra]}")

