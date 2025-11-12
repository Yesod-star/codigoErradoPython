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
        if not notas:
            return 0
        soma = 0
        for n in notas:
            soma += n
        media = soma / len(notas)
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!")
        return
    print("===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        print("Nome:", aluno)
        print("Notas:", alunos[aluno])
        print("Média:", calcular_media(aluno))
        print("----------------------")


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
        print("Remoção concluída!")
    else:
        print("Aluno não existe")


def salvar_dados():
    with open("alunos.txt", "w") as arquivo:
        for nome in alunos:
            linha = nome + ":" + ",".join(map(str, alunos[nome])) + "\n"
            arquivo.write(linha)


def carregar_dados():
    try:
        with open("alunos.txt") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(":")
                nome = partes[0]
                notas_str = partes[1] if len(partes) > 1 else ""
                if notas_str:
                    notas = [float(n) for n in notas_str.split(",")]
                else:
                    notas = []
                alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except:
        print("Erro ao carregar dados!")


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
