# Programa de cadastro de alunos e cálculo de médias

alunos = {}  # dicionário de alunos: nome -> lista de notas


def adicionar_aluno(nome):
    """Adiciona um novo aluno ao dicionário."""
    if nome in alunos:
        print("Aluno já existe!")
    else:
        alunos[nome] = []
        print(f"Aluno '{nome}' adicionado com sucesso!")


def adicionar_nota(nome, nota):
    """Adiciona uma nota a um aluno existente."""
    if nome not in alunos:
        print("Aluno não encontrado!")
        return

    if nota < 0 or nota > 10:  # corrigido: OR em vez de AND
        print("Nota inválida! (deve estar entre 0 e 10)")
    else:
        alunos[nome].append(nota)
        print(f"Nota {nota} adicionada ao aluno '{nome}' com sucesso!")


def calcular_media(nome):
    """Calcula e retorna a média de notas de um aluno."""
    if nome not in alunos:
        print("Aluno não existe!")
        return None

    notas = alunos[nome]
    if not notas:  # verifica lista vazia
        print(f"O aluno '{nome}' ainda não tem notas cadastradas.")
        return 0.0

    soma = sum(notas)
    media = soma / len(notas)
    return media


def mostrar_alunos():
    """Exibe todos os alunos, suas notas e médias."""
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return

    print("\n===== LISTA DE ALUNOS =====")
    for aluno, notas in alunos.items():
        media = calcular_media(aluno)
        print(f"Nome: {aluno}")
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")
        print("----------------------")


def remover_aluno(nome):
    """Remove um aluno do cadastro."""
    if nome in alunos:
        alunos.pop(nome)
        print(f"Aluno '{nome}' removido com sucesso.")
    else:
        print("Aluno não existe.")


def salvar_dados():
    """Salva os dados dos alunos em um arquivo."""
    try:
        with open("alunos.txt", "w", encoding="utf-8") as arquivo:
            for nome, notas in alunos.items():
                linha = f"{nome}:{','.join(map(str, notas))}\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar os dados:", e)


def carregar_dados():
    """Carrega os dados do arquivo 'alunos.txt'."""
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, notas_str = linha.strip().split(":")
                if notas_str.strip():
                    notas = [float(n) for n in notas_str.split(",")]
                else:
                    notas = []
                alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'alunos.txt' não encontrado.")
    except Exception as e:
        print("Erro ao carregar dados:", e)


def menu():
    """Exibe o menu principal e gerencia as opções."""
    while True:
        print("\n==== MENU ====")
        print("1 - Adicionar alunos")
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
            nome = input("Nome do aluno: ")
            try:
                nota = float(input("Nota (0 a 10): "))
                adicionar_nota(nome, nota)
            except ValueError:
                print("Erro: digite um número válido para a nota.")

        elif opcao == "3":
            mostrar_alunos()

        elif opcao == "4":
            nome = input("Nome do aluno: ")
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



    menu()
