alunos = {}  # dicionário de alunos: nome -> lista de notas


def adicionar_aluno(nome):
    if nome in alunos:
        print("Aluno já existe!")
    else:
        alunos[nome] = []
        print(f"Aluno '{nome}' adicionado com sucesso.")


def adicionar_nota(nome, nota):
    if nome not in alunos:
        print("Aluno não encontrado!")
    else:
        if nota < 0 or nota > 10:
            print("Nota inválida! (deve estar entre 0 e 10)")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome not in alunos:
        print("Aluno não existe.")
        return None

    notas = alunos[nome]
    if len(notas) == 0:
        print(f"Aluno '{nome}' não possui notas ainda.")
        return None

    soma = sum(notas)
    media = soma / len(notas)
    return media


def mostrar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!")
        return

    print("\n===== LISTA DE ALUNOS =====")
    for aluno, notas in alunos.items():
        media = calcular_media(aluno)
        media_str = f"{media:.2f}" if media is not None else "-"
        print(f"Nome: {aluno}")
        print(f"Notas: {notas}")
        print(f"Média: {media_str}")
        print("----------------------")


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print(f"Aluno '{nome}' removido com sucesso.")
    else:
        print("Aluno não existe.")


def salvar_dados():
    try:
        with open("alunos.txt", "w") as arquivo:
            for nome, notas in alunos.items():
                linha = nome + ":" + ",".join(map(str, notas)) + "\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar dados:", e)


def carregar_dados():
    try:
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ":" in linha:
                    nome, notas_str = linha.split(":")
                    notas = [float(n) for n in notas_str.split(",") if n]
                    alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Nenhum dado carregado.")
    except Exception as e:
        print("Erro ao carregar dados:", e)


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
            try:
                nota = float(input("Nota: "))
                adicionar_nota(nome, nota)
            except ValueError:
                print("Por favor, insira um número válido para a nota.")
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
            print("Opção inválida! Tente novamente.")


# Executa o programa
menu()
