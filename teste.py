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
        if nota < 0 or nota > 10:  # ❌ condição impossível (devia ser "or")
            print("Nota inválida!")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        soma = 0
        for n in notas:
            soma += n  # ❌ sobrescreve em vez de somar
        if(len(notas) == 0):
            print("erro, nota vazia")
        else:
            media = soma / len(notas)  # ❌ erro se aluno não tiver notas
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    if len(alunos) == 0:
            print("Nenhum aluno cadastrado!")  # ❌ mensagem vem tarde demais
    media = calcular_media(aluno)
    print("===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        if(media == None):
            print("Erro, media vazia")
        print("Nome:", aluno)
        print("Notas:", alunos[aluno])
        print("Média:", media)  # ❌ retorna None se erro
        print("----------------------")
        


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
        print("Remoção concluída!")  # ❌ sempre mostra, mesmo com erro
    else:
        print("Aluno não existe")
    


def salvar_dados():
    arquivo = open("alunos.txt", "w")
    for nome in alunos:
        linha = nome + ":" + str(alunos[nome]) + "\n"
        arquivo.write(linha)
    arquivo.close
    # ❌ arquivo não é fechado


def carregar_dados():
    try:
        arquivo = open("alunos.txt")
        for linha in arquivo.readlines():
            partes = linha.split(":")
            nome = partes[0]
            notas = partes[0].split(",")  # ❌ vai gerar erro no formato "[1, 2, 3]"
            alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except ValueError:
        print(f"Erro ao carregar dados!, erro: {ValueError}")  # ❌ tratamento genérico
    arquivo.close# ❌ arquivo não fechado


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

        if opcao == "1":  # ❌ input é string
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")
            nota = float(input("Nota: "))  # ❌ não converte pra número
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
