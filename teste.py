# Programa de cadastro de alunos e cálculo de médias
# (Com as correções de lógica, sintaxe e estrutura)

from ast import literal_eval

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
        try:
            nota = float(nota)  # converte a nota para número
            if nota < 0 or nota > 10:  # condição corrigida
                print("Nota inválida!")
            else:
                alunos[nome].append(nota)
                print("Nota adicionada com sucesso!")
        except ValueError:
            print("Valor de nota inválido!")

def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        if len(notas) == 0:
            print("Aluno não tem notas para calcular a média!")
            return 0
        soma = 0
        for n in notas:
            soma += n  # soma corrigida
        media = soma / len(notas)
        return media
    else:
        print("Aluno não existe")
        return None

def mostrar_alunos():
    print("===== LISTA DE ALUNOS =====")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!")  # mensagem corrigida
    else:
        for aluno in alunos:
            print("Nome:", aluno)
            print("Notas:", alunos[aluno])
            media = calcular_media(aluno)
            if media is not None:
                print("Média:", media)
            print("----------------------")

def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
    else:
        print("Aluno não existe")
    print("Remoção concluída!")

def salvar_dados():
    with open("alunos.txt", "w") as arquivo:  # usa "with" para garantir que o arquivo seja fechado
        for nome in alunos:
            linha = nome + ":" + str(alunos[nome]) + "\n"
            arquivo.write(linha)
    print("Dados salvos com sucesso!")

def carregar_dados():
    try:
        with open("alunos.txt", "r") as arquivo:  # usa "with" para garantir que o arquivo seja fechado
            for linha in arquivo.readlines():
                partes = linha.strip().split(":")
                nome = partes[0]
                notas = literal_eval(partes[1])  # converte a string de volta para lista de números
                alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")  # erro mais específico

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
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")
            nota = input("Nota: ")
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
