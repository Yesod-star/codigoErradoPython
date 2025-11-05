# Programa de cadastro de alunos e cálculo de médias (versão corrigida)

alunos = {}  # dicionário: nome -> lista de notas


def adicionar_aluno(nome):
    if nome in alunos:
        print("Aluno já existe!")
    else:
        alunos[nome] = []
        print(f"Aluno {nome} adicionado com sucesso.")


def adicionar_nota(nome, nota):
    if nome not in alunos:
        print("Aluno não encontrado!")
    else:
        if nota < 0 or nota > 10:  # ✅ corrigido "and" -> "or"
            print("Nota inválida! Deve estar entre 0 e 10.")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        if len(notas) == 0:  # ✅ evita divisão por zero
            return 0
        soma = 0
        for n in notas:
            soma += n  # ✅ corrigido: soma acumulativa
        media = soma / len(notas)
        return media
    else:
        print("Aluno não existe.")
        return None


def mostrar_alunos():
    if len(alunos) == 0:  # ✅ mensagem colocada antes do loop
        print("Nenhum aluno cadastrado!")
        return

    print("\n===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        media = calcular_media(aluno)
        print(f"Nome: {aluno}")
        print(f"Notas: {alunos[aluno]}")
        print(f"Média: {media:.2f}")
        print("----------------------")


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso.")
    else:
        print("Aluno não existe.")
    # ✅ removida mensagem redundante


def salvar_dados():
    try:
        with open("alunos.txt", "w") as arquivo:  # ✅ usa 'with' para fechar automático
            for nome in alunos:
                notas_str = ",".join(map(str, alunos[nome]))
                arquivo.write(f"{nome}:{notas_str}\n")
        print("Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar dados:", e)


def carregar_dados():
    try:
        with open("alunos.txt", "r") as arquivo:  # ✅ usa 'with' e leitura correta
            for linha in arquivo:
                partes = linha.strip().split(":")
                if len(partes) == 2:
                    nome = partes[0]
                    notas_str = partes[1].split(",") if partes[1] else []
                    notas = [float(n) for n in notas_str if n.strip() != ""]
                    alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo encontrado. Começando novo cadastro.")
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

        if opcao == "1":  # ✅ corrigido: comparação com string
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")
            try:
                nota = float(input("Nota: "))  # ✅ converte para número
                adicionar_nota(nome, nota)
            except ValueError:
                print("Digite um valor numérico para a nota.")
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
