import os
import random
import time

os.system('cls')
ganhou ="n"
tentativas = 0
JN = "S"
t= [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]

class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message = message
        
def verificavitoria():
    global ganhou
    if (t[0][0]) == (t[0][1]) == (t[0][2])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    elif (t[1][0]) == (t[1][1]) == (t[1][2])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    elif (t[2][0]) == (t[2][1]) == (t[2][2])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    if (t[0][0]) == (t[1][0]) == (t[2][0])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    elif (t[0][1]) == (t[1][1]) == (t[2][1])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    elif (t[0][2]) == (t[1][2]) == (t[2][2])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    if (t[0][0]) == (t[1][1]) == (t[2][2])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    elif (t[2][0]) == (t[1][1]) == (t[0][2])== "X":
        print("O jogador X venceu")
        ganhou = "s"
    if (t[0][0]) == (t[0][1]) == (t[0][2])== "O":
        print("O jogador 'O'venceu")
        ganhou = "s"
    elif (t[1][0]) == (t[1][1]) == (t[1][2])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    elif (t[2][0]) == (t[2][1]) == (t[2][2])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    if (t[0][0]) == (t[1][0]) == (t[2][0])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    elif (t[0][1]) == (t[1][1]) == (t[2][1])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    elif (t[0][2]) == (t[1][2]) == (t[2][2])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    if (t[0][0]) == (t[1][1]) == (t[2][2])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    elif (t[2][0]) == (t[1][1]) == (t[0][2])== "O":
        print("O jogador 'O' venceu")
        ganhou = "s"
    return ganhou

def Menu():
    print("Deseja jogar sozinho ou com mais 1 jogador?"
    ,"\n", "1 - Para jogar Sozinho.", "\n", "2 - Para jogar com mais alguem.",
    "\n", "3 - Para sair.")
    try:
        opc = int(input("Escolha: "))
        if opc > 3:
            raise InputError("Valor Invalido, digite apenas os numeros 1,2 ou 3")  
        elif opc < 1:
            raise InputError("Valor Invalido, digite apenas os numeros 1,2 ou 3")
    except ValueError:
        print("Valor Invalido, digite apenas os numeros 1,2 ou 3")
        time.sleep(2)
        os.system('cls')
        Menu()
    except InputError:
        print("Valor Invalido, digite apenas os numeros 1,2 ou 3")
        time.sleep(2)
        os.system('cls')
        Menu()

def JogadaDaPessoaO():
     print("JOGADOR 'O'")
     print("tentativas: ", tentativas);
     continuar = "s"
     while continuar == "s":
        y = input("Digite uma linha: ");
        z = input("Digite uma coluna: ");
        if t[int(y)][int(z)] == " ":
            t[int(y)][int(z)] = "O"
            continuar = "n"
            break
        else:
            print("Você digitou em um lugar que ja foi feita uma jogada\nTente novamente")
            time.sleep(2)
            continuar = "s"
     LimparTela()

def MostrarJogo():
    (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
    "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
    "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));

def JogadaBot():
    continuar = "s"
    while continuar == "s":
        y = random.randrange(0, 2)
        z = random.randrange(0, 2)
        if t[int(y)][int(z)] == " ":
            t[int(y)][int(z)] = "O"
            continuar = "n"
            break
        else:
            continuar = "s"
    LimparTela()

def JogadaDaPessoaX():
    print("JOGADOR 'X'")
    print("tentativas: ", tentativas);
    continuar = "s"
    while continuar == "s":
        y = input("Digite uma linha: ");
        z = input("Digite uma coluna: ");
        if t[int(y)][int(z)] == " ":
            t[int(y)][int(z)] = "X"
            continuar = "n"
            break
        else:
            print("Você digitou em um lugar que ja foi feita uma jogada\nTente novamente")
            time.sleep(2)
            continuar = "s"
    LimparTela()

def Jogo1():
    global tentativas
    while ganhou != "s":
            if tentativas == 9:
                break
            else:
                pass
            # JOGADOR "X"
            JogadaDaPessoaX()

            MostrarJogo()

            verificavitoria()
            tentativas += 1;

            # JOGADA DO BOT
            if ganhou =="s":
                break
            else:
                pass
            time.sleep(1/2)
            JogadaBot()

            MostrarJogo()
            verificavitoria()
            tentativas += 1;

def Jogo2():
    global tentativas
    while ganhou !="s":
            if tentativas == 9:
                break
            else:
                pass 
            # JOGADOR "X"
            JogadaDaPessoaX()

            MostrarJogo()

            verificavitoria()

            tentativas += 1;

            # JOGADA DO jogador 2
            if ganhou =="s":
                break
            else:
                pass
            JogadaDaPessoaO()

            MostrarJogo()

            verificavitoria()

            tentativas += 1;

def LimparTela():
    os.system('cls')

def jogarsozinho():
    global ganhou
    global t
    global JN
    global tentativas

    print("O jogador 'x' é quem começa, se decidiu por jogar sozinho você é o jogador 'x'.")

    MostrarJogo()

    while JN == "S":
        #RESETANDO O VALOR DE GANHOU E DE T PARA O JOGO RODAR NOVAMENTE
        ganhou = "n"
        t = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
         ]
        Jogo1()

        JN = input("Jogar Novamente? (S/N): ")

        tentativas = 0

    print("Obrigado por jogar\nFechando...")

    time.sleep(3);LimparTela()
    
def jogarcomalguem():
    global ganhou
    global t
    global JN
    global tentativas

    print("O jogador 'x' é quem começa, se decidiu por jogar sozinho você é o jogador 'x'.")

    MostrarJogo()

    while JN == "S":
        # RESETANDO O VALOR DE TENTATIVAS E DE GANHOU PARA O JOGO RODAR NOVAMENTE
        tentativas = 0
        ganhou = "n"
        t = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        Jogo2()
        
        JN = input("Jogar Novamente? (S/N): ")

        tentativas = 0

    print("Obrigado por jogar\nFechando...")

    time.sleep(3);LimparTela()
    
ret = Menu()
while int(ret) < 4:
    if ret == 1:
        jogarsozinho()
    elif ret == 2:
        jogarcomalguem()
    elif ret == 3:
        print("Saindo...")
        time.sleep(3)
        break
    ret = Menu()
    LimparTela()
print("Programa Finalizado")
