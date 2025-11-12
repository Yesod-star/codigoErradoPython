# Programa de cadastro de alunos e cálculo de médias
# (Contém muitos erros de lógica, sintaxe e estrutura)

alunos = {}  # dicionário de alunos: nome -> lista de notas


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


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        soma = 0
        if notas == 0:
            print("Aluno não possui nota")
        else :
            for n in notas:
                soma += n 
                print(soma) 
            media = soma / len(notas) 

        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    print("===== LISTA DE ALUNOS =====")
    if len(alunos) == 0:
            print("Nenhum aluno cadastrado!")
    else:
        for aluno in alunos:
            print("Nome:", aluno)
            print("Notas:", alunos[aluno])
            print("Média:", calcular_media(aluno))  
            print("----------------------")

   


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
    else:
        print("Aluno não existe")
     


def salvar_dados():
    arquivo = open("alunos.txt", "w") 
    for nome, notas in alunos():
        linha = "{nome}" + ":" + str(alunos[nome]) + "\n"
        arquivo.write(linha)
        arquivo.close()
    


def carregar_dados():
    try:
        arquivo = open("alunos.txt", "r")
        for linha in arquivo.readlines():
             linha = linha.strip()
             if not linha:
                    continue
             nome, notas_str = linha.split(":")
             notas = [float(n) for n in notas_str.split(",") if n]
             alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except:
        print("Erro ao carregar dados!")  
        arquivo.close()


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

        if opcao == "1":  
            nome = input(str("Nome do aluno: "))
            adicionar_aluno(nome)

        elif opcao == "2":
            nome = input("Nome: ")
            nota = input(float("Nota: ")) 
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
