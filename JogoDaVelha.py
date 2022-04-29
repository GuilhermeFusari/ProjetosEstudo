import os
import random
import time

os.system('cls')
t = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

print ("Bem vindo ao jogo da velha")
print("Deseja jogar sozinho ou com mais 1 jogador?"
,"\n","1 - Para jogar Sozinho.","\n","2 - Para jogar com mais alguem.")
escolha = input("Escolha: ")
os.system('cls')
if escolha == "1":
    print("O jogador 'x' é quem começa, se decidiu por jogar sozinho você é o jogador 'x'.")
    (print( "     0   1   2","\n","0 -",t[0][0], "|", t[0][1], "|",t[0][2],
    "\n ", "   ----------", "\n","1 -", t[1][0], "|", t[1][1], "|",t[1][2],
    "\n",  "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|",t[2][2]));
    JN = "S"
    while JN == "S":
        t = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]
        tentativas = 0
        while tentativas < 9: 
            #JOGADOR "X"
            print("tentativas: ",tentativas);

            y = input("Digite uma linha: ");
            z = input("Digite uma coluna: ");

            t[int(y)][int(z)] ="X";

            (os.system('cls'));

            (print( "     0   1   2","\n","0 -",t[0][0], "|", t[0][1], "|",t[0][2],
            "\n ", "   ----------", "\n","1 -", t[1][0], "|", t[1][1], "|",t[1][2],
            "\n",  "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|",t[2][2]));
            
            if (t[0][0]) == "X" == (t[0][1]) == (t[0][2]):
                print("O jogador X venceu")
                break
       
            elif (t[1][0]) == "X" == (t[1][1]) == (t[1][2]):
                print("O jogador X venceu")
                break
       
            elif (t[2][0]) == "X" == (t[2][1]) == (t[2][2]):
                print("O jogador X venceu")
                break
            if (t[0][0]) == "X" == (t[1][0]) == (t[2][0]):
                print("O jogador X venceu")
                break
       
            elif (t[0][1]) == "X" == (t[1][1]) == (t[2][1]):
                print("O jogador X venceu")
                break
       
            elif (t[0][2]) == "X" == (t[1][2]) == (t[2][2]):
                print("O jogador X venceu")
                break 
            if (t[0][0]) == "X" == (t[1][1]) == (t[2][2]):
                print("O jogador X venceu")
                break
            
            elif(t[2][0]) == "X" == (t[1][1]) == (t[0][2]):
                print("O jogador X venceu")
                break
            tentativas+=1;

            #JOGADA DO BOT
           
            continuar = "s"
            while continuar == "s":
                y = random.randrange(0,2)
                x = random.randrange(0,2)
                if t[int(y)][int(z)] ==" ":
                    t[int(y)][int(z)] ="O"
                    continuar = "n"
                    break
                else:
                    continuar ="s"
            
            (os.system('cls'));

            (print( "     0   1   2","\n","0 -",t[0][0], "|", t[0][1], "|",t[0][2],
            "\n ", "   ----------", "\n","1 -", t[1][0], "|", t[1][1], "|",t[1][2],
            "\n",  "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|",t[2][2]));
            if (t[0][0]) == "O" == (t[0][1]) == (t[0][2]):
                print("Você Perdeu")
                break
       
            elif (t[1][0]) == "O" == (t[1][1]) == (t[1][2]):
                print("Você Perdeu")
                break
       
            elif (t[2][0]) == "O" == (t[2][1]) == (t[2][2]):
                print("Você Perdeu")
                break
            if (t[0][0]) == "O" == (t[1][0]) == (t[2][0]):
                print("Você Perdeu")
                break
       
            elif (t[0][1]) == "O" == (t[1][1]) == (t[2][1]):
                print("Você Perdeu")
                break
       
            elif (t[0][2]) == "O" == (t[1][2]) == (t[2][2]):
                print("Você Perdeu")
                break 
            if (t[0][0]) == "O" == (t[1][1]) == (t[2][2]):
                print("Você Perdeu")
                break
            
            elif(t[2][0]) == "O" == (t[1][1]) == (t[0][2]):
                print("Você Perdeu")
                break

            

            tentativas+=1;
            

            

    
        JN = input("Jogar Novamente? (S/N): ")
    print (" Obrigado por jogar","\n","Fechando...")
    time.sleep(3)
    os.system('cls')
elif escolha == "2":
    print("O jogador 'x' é quem começa, se decidiu por jogar sozinho você é o jogador 'x'.")
    (print( "     0   1   2","\n","0 -",t[0][0], "|", t[0][1], "|",t[0][2],
    "\n ", "   ----------", "\n","1 -", t[1][0], "|", t[1][1], "|",t[1][2],
    "\n",  "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|",t[2][2]));
    JN = "S"
    while JN == "S":
        t = [
     [" "," "," "],
     [" "," "," "],
     [" "," "," "]
     ]
        tentativas = 0
        while tentativas < 9: 
            #JOGADOR "X"
            print("tentativas: ",tentativas);

            y = input("Digite uma linha: ");
            z = input("Digite uma coluna: ");

            t[int(y)][int(z)] ="x";

            (os.system('cls'));

            (print( "     0   1   2","\n","0 -",t[0][0], "|", t[0][1], "|",t[0][2],
            "\n ", "   ----------", "\n","1 -", t[1][0], "|", t[1][1], "|",t[1][2],
            "\n",  "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|",t[2][2]));
            if (t[0][0]) == "x" == (t[0][1]) == (t[0][2]):
                  print("O jogador X venceu")
                  break
       
            elif (t[1][0]) == "x" == (t[1][1]) == (t[1][2]):
                 print("O jogador X venceu")
                 break
       
            elif (t[2][0]) == "x" == (t[2][1]) == (t[2][2]):
                print("O jogador X venceu")
                break
            if (t[0][0]) == "x" == (t[1][0]) == (t[2][0]):
                print("O jogador X venceu")
                break
       
            elif (t[0][1]) == "x" == (t[1][1]) == (t[2][1]):
                print("O jogador X venceu")
                break
       
            elif (t[0][2]) == "x" == (t[1][2]) == (t[2][2]):
                print("O jogador X venceu")
                break 
            if (t[0][0]) == "x" == (t[1][1]) == (t[2][2]):
                print("O jogador X venceu")
                break
            
            elif(t[2][0]) == "x" == (t[1][1]) == (t[0][2]):
                print("O jogador X venceu")
                break

            tentativas+=1;

            #JOGADA DO jogador 2
            print("tentativas: ",tentativas);

            y = input("Digite uma linha: ");
            z = input("Digite uma coluna: ");

            t[int(y)][int(z)] ="O";

            (os.system('cls'));

            (print( "     0   1   2","\n","0 -",t[0][0], "|", t[0][1], "|",t[0][2],
            "\n ", "   ----------", "\n","1 -", t[1][0], "|", t[1][1], "|",t[1][2],
            "\n",  "   ----------", "\n", "2 -", t[2][0], "|", t[2][1], "|",t[2][2]));
            
            if (t[0][0]) == "O" == (t[0][1]) == (t[0][2]):
                  print("O jogador 'O' venceu")
                  break
       
            elif (t[1][0]) == "O" == (t[1][1]) == (t[1][2]):
                 print("O jogador 'O' venceu")
                 break
       
            elif (t[2][0]) == "O" == (t[2][1]) == (t[2][2]):
                print("O jogador 'O' venceu")
                break
            if (t[0][0]) == "O" == (t[1][0]) == (t[2][0]):
                print("O jogador 'O' venceu")
                break
       
            elif (t[0][1]) == "O" == (t[1][1]) == (t[2][1]):
                print("O jogador 'O' venceu")
                break
       
            elif (t[0][2]) == "O" == (t[1][2]) == (t[2][2]):
                print("O jogador 'O' venceu")
                break 
            if (t[0][0]) == "O" == (t[1][1]) == (t[2][2]):
                print("O jogador 'O' venceu")
                break
            
            elif(t[2][0]) == "O" == (t[1][1]) == (t[0][2]):
                print("O jogador 'O' venceu")
                break

            tentativas+=1;
            

            

    
        JN = input("Jogar Novamente? (S/N): ")
    print (" Obrigado por jogar","\n","Fechando...")
    time.sleep(3)
    os.system('cls')
else:
    print("Numero invalido")
    
    

