import os
import random
import time

os.system('cls')
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
ganhou ="n"
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
os.system('cls')
def jogarsozinho():
    global ganhou
    global t
    print("O jogador 'x' é quem começa, se decidiu por jogar sozinho você é o jogador 'x'.")
    (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
        "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
        "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));
    JN = "S"
    while JN == "S":
        ganhou = "n"
        t = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
         ]
        tentativas = 0
        while ganhou != "s":
            if tentativas == 9:
                break
            else:
                pass
            # JOGADOR "X"
            print("SUA JOGADA")
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

            (os.system('cls'));

            (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
                "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
                "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));

            verificavitoria()
            tentativas += 1;

            # JOGADA DO BOT
            if ganhou =="s":
                break
            else:
                pass
            time.sleep(1/2)
            continuar = "s"
            while continuar == "s":
                y = random.randrange(0, 2)
                x = random.randrange(0, 2)
                if t[int(y)][int(z)] == " ":
                    t[int(y)][int(z)] = "O"
                    continuar = "n"
                    break
                else:
                    continuar = "s"

            (os.system('cls'));

            (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
                "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
                "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));
            verificavitoria()
            tentativas += 1;

        JN = input("Jogar Novamente? (S/N): ")
    print("Obrigado por jogar\nFechando...")
    time.sleep(3)
    os.system('cls')
    
def jogarcomalguem():
    global ganhou
    global t
   
    print("O jogador 'x' é quem começa, se decidiu por jogar sozinho você é o jogador 'x'.")
    (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
        "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
        "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));
    JN = "S"
    while JN == "S":
        t = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        tentativas = 0
        while ganhou !="s":
            if tentativas == 9:
                break
            else:
                pass 
            # JOGADOR "X"
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
            (os.system('cls'));

            (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
                "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
                "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));
            verificavitoria()

            tentativas += 1;

            # JOGADA DO jogador 2
            if ganhou =="s":
                break
            else:
                pass
            print("JOGADOR 'O'")
            print("tentativas: ", tentativas);
            print("Ganhou: ",ganhou)
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

            (os.system('cls'));

            (print("     0   1   2", "\n", "0 -", t[0][0], "|", t[0][1], "|", t[0][2],
                "\n ", "   ----------", "\n", "1 -", t[1][0], "|", t[1][1], "|", t[1][2],
                "\n", "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|", t[2][2]));
            verificavitoria()
            tentativas += 1;

        JN = input("Jogar Novamente? (S/N): ")
    print("Obrigado por jogar\nFechando...")
    time.sleep(3)
    os.system('cls')
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
    os.system('cls')
print("Programa Finalizado")
