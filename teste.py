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
        if nota < 0 or nota > 10: # Corrigido o operador lógico
            print("Nota inválida!")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        soma = 0
        for n in notas:
            soma = soma + n  # Corrigido operador de soma
        media = soma / len(notas) if len(notas) > 0 else 0  # Corrigido divisão por zero
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    print("===== LISTA DE ALUNOS =====")
    
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado!")  # Corrigido condição
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
        print("Remoção concluída!")
    else:
        print("Aluno não existe")



def salvar_dados():
    arquivo = open("alunos.txt", "w")
    for nome in alunos:
        linha = nome + ":" + str(alunos[nome]) + "\n"
        arquivo.write(linha)
    arquivo.close()  # Corrigido fechamento do arquivo


def carregar_dados():
    try:
        arquivo = open("alunos.txt")
        for linha in arquivo.readlines():
            partes = linha.split(":")
            nome = partes[0]
            notas_str = partes[1].strip().strip("[]").split(",")
            notas = [float(nota) for nota in notas_str if nota]  # Corrigido conversão para float
            alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except Exception as e:
        print("Erro ao carregar dados:", e)
    finally:
        arquivo.close()  # Corrigido fechamento do arquivo


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

        if opcao == "1":  # Corrigido operador de comparação
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")
            nota = int(input("Nota: ")) # Corrigido para int
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
