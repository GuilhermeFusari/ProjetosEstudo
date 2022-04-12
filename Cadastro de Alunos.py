import os
os.system('cls')
alunos = []
class aluno:
    media = 0
    passou = False
    nome =""
    def __init__(self,m,p,n):
        self.media = m
        self.passou = p
        self.nome = n
    def info(self):
        aprovacao = "Aprovado" if self.media >= 6 else "Reprovado"
        print("Aluno(a):", self.nome, "\nMédia:", str(self.media), "\nEle(a) está:", str(aprovacao))
        print("------------------------")



def Menu():
    print("1 - Cadastrar Novo Aluno")
    print("2 - Listar Alunos")
    print("3 - Informações do Aluno")
    print("4 - Excluir aluno do cadastro")
    print("5 - Listar todos alunos e informações ")
    print("6 - Sair")
    opc = input("Dgite uma opção: ")
    return opc


def Novo_aluno():
    os.system('cls')
    n = input("Nome do Aluno: ")
    p = False
    m = input("Média do Aluno: ")
    al = aluno(int(m),p,n)
    alunos.append(al)
    print("Aluno cadastrado")
    os.system("pause")



def Informacoes():
    os.system('cls')
    a = input("Digite o numero do Aluno que deseja ver as informaçoes: ")
    try:
        alunos[int(a)].info()
    except:
        print("Aluno não existe no cadastro")
    os.system("pause")



def ExcluirAluno():
    os.system('cls')
    a = input("Digite o numero do Aluno que deseja excluir do cadastro: ")
    try:
        del alunos[int(a)]
    except:
        print("Aluno não existe no cadastro")
    os.system("pause")


def listarAlunos():
     os.system('cls')
     p = 0
     for i in alunos:
         print(str(p) + " -" , i.nome)
         p = p+1
     os.system("pause")


def listartudo():
    os.system('cls')
    for i in alunos:
        i.info()
    os.system("pause")
ret = Menu()
while ret < "6":
    if ret == "1":
        Novo_aluno()
    elif ret == "2":
        listarAlunos()
    elif ret == "3":
        Informacoes()
    elif ret == "4":
        ExcluirAluno()
    elif ret == "5":
        listartudo()
    ret = Menu()
os.system('cls')
print("Finalizando o programa....\nPrograma finalizado!")

