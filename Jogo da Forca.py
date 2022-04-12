import os
import time
os.system('cls')
print("================================\nOlá bem vindo ao jogo da forca\n================================")
print("Você precisa de no mínimo 2 jogadores\nUm deles vai escolher uma palavra e o outro tentar acertar a palavra esocolhida!")
time.sleep(4)
palavra = input ("Jogador 1 digite uma palavra: ")
letras_escolhidas = []
estado_da_palavra = ["_"]*len(palavra)
os.system('cls')
print("a palavra escolhida tem {} letras".format(len(palavra)))
erros = 6
while ''.join(estado_da_palavra) != palavra or erros == 0 :
    chute = input("Jogador 2 chute uma letra: ")
    letras_escolhidas.append(chute)
    print ("letras_escohidas" + str(letras_escolhidas))
    if chute in palavra:
        print("você acertou uma letra na posição {}".format(palavra.index(chute)))
        for i in range (len(palavra)):
            if chute == palavra[i]:
             estado_da_palavra[i] = chute
        print(estado_da_palavra)
        time.sleep(2)
    elif erros == 0:
        break
    else:
        erros = erros -1
        print("voce errou")
        print("erros restantes:", erros)

         
         
        time.sleep(2)
if ''.join(estado_da_palavra) == palavra:
    print("\n\nvoce ganhou, a palavra era "+palavra)
else:
    print ("\n\nvoce perdeu pois suas tentativas acabaram")
    print("a palavra era "+palavra)