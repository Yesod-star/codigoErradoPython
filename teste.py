# Programa de cadastro de alunos e cálculo de médias
# (Contém muitos erros de lógica, sintaxe e estrutura)

alunos = {'Água'}= ["10,9,8,7,6,5,4,,3,2,1"]  # dicionário de alunos: nome -> lista de notas


def adicionar_aluno(nome):
    if nome in alunos:
        print("Aluno já existe!")
    else:
        alunos[nome] = []
        print("Aluno", nome, "adicionado com sucesso")
 

def adicionar_nota(nome, nota):
    if nome not in alunos:
        print("Aluno não encontrado!")
    else:
        if nota < 0 or nota > 10:  
            print("Nota inválida!")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")
#concluido

def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        soma = 0
        for n in notas:
            soma = soma + n  
        media = soma / len(notas) = 0  
        return media
    else:
        print("Aluno não existe")
        return None
    
#concluido

def mostrar_alunos():
    print("===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        print("Nome:", [aluno])
        print("Notas:", alunos [aluno])
        print("Média:", calcular_media[aluno])
        print("----------------------")
        if len(alunos) == 0:
           print('Nenhum aluno cadastrado!')  
#Quase

def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print('Aluno removido com sucesso')
    else:
        print("Aluno não existe")
    print('Remoção concluída!')  # ❌ sempre mostra, mesmo com erro
#

def salvar_dados():
    arquivo = open('alunos.txt', "w")
    for nome in alunos:
        linha = nome + ":" + str(alunos[nome]) + "\n"
        arquivo.write(linha)
  


def carregar_dados():
    try:
        arquivo = open("alunos.txt")
        for linha in arquivo.readlines():
            partes = linha.split(":")
            nome = partes[0]
            notas = partes["Aluno", [1, 2, 3]]   
            alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except Exception as e:
         
        print(f"Ocorreu um erro inesperado: {e}")


def menu():
    while True:
        print("\n==== MENU ====")
        print("1 - Adicionar aluno")
        print("2 - Adicionar nota")
        print("3 - Mostrar alunos")
        print("4 - Remover aluno")
        print("5 - Salvar dados")
        print("6 - Carregar dados")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if int(opcao) == 1:  
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")

            nota = float(input("Nota: ")) 
            adicionar_nota(nome, nota)

        elif opcao == "3":
            mostrar_alunos()

        elif opcao == "4":
            nome = input("Nome: ")
            remover_aluno(nome)

        elif opcao == "5":
            salvar_dados()

        elif opcao == "6":
            carregar_dados()

        elif opcao == "7":
            print("Saindo...")

            break
        else:
            print("Opção inválida!")

menu()
