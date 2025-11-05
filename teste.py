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
        if nota < 0 or nota > 10:  # ✅condição impossível (devia ser "or")
            print("Nota inválida!")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        if len(notas) == 0:
            print("Aluno ainda não tem notas cadastradas.")
            return None
        soma = sum(notas)   # ✅sobrescreve em vez de somar
        media = soma / len(notas)  # ✅erro se aluno não tiver notas
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    media = 0
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!")  # ✅mensagem vem tarde demais
        return

    print("===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        print("Nome:", aluno)
        print("Notas:", alunos[aluno])
        print("Média:", calcular_media(aluno))  # ✅retorna None se erro
        print("----------------------")

def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
        print("Remoção concluída!")  # ✅sempre mostra, mesmo com erro
    else:
        print("Aluno não existe")
    


def salvar_dados():
    try:
        with open("alunos.txt", "w") as arquivo:
            for nome in alunos:
                linha = nome + ":" + ",".join(map(str, alunos[nome])) + "\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar dados:", e)
    # ✅arquivo não é fechado


def carregar_dados():
    try:
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ":" in linha:
                    nome, notas_str = linha.split(":")
                    if notas_str.strip():
                        notas = [float(x) for x in notas_str.split(",")]   # ✅vai gerar erro no formato "[1, 2, 3]"
                    else:
                        notas = []
                    alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum dado carregado.")
    except Exception as e: 
        print("Erro ao carregar dados:", e)  # ✅tratamento genérico
    # ✅arquivo não fechado

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

        if opcao == "1":  # ✅input é string
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")
            nota = input("Nota: ")  # ✅não converte pra número
            notaI = int(nota)
            adicionar_nota(nome, notaI)
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
