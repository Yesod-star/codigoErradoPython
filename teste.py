# Programa de cadastro de alunos e cálculo de médias
# (Agora corrigido e funcionando)

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
        # Corrigido: agora verifica se a nota está entre 0 E 10
        if nota < 0 or nota > 10:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        # Corrigido: verifica se o aluno tem notas antes de calcular
        if len(notas) == 0:
            print(f"Aluno {nome} não possui notas cadastradas.")
            return 0
        
        soma = 0
        for n in notas:
            soma += n  # Corrigido: agora SOMA as notas em vez de sobrescrever
        media = soma / len(notas)
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    print("===== LISTA DE ALUNOS =====")
    
    # Corrigido: verifica primeiro se há alunos cadastrados
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!")
        return
    
    for aluno in alunos:
        print("Nome:", aluno)
        print("Notas:", alunos[aluno])
        media = calcular_media(aluno)
        # Corrigido: só mostra a média se não for None
        if media is not None:
            print(f"Média: {media:.2f}")
        print("----------------------")


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
    else:
        print("Aluno não existe")
    # Removido o print desnecessário que sempre aparecia


def salvar_dados():
    try:
        # Corrigido: usando with para fechar automaticamente o arquivo
        with open("alunos.txt", "w") as arquivo:
            for nome in alunos:
                linha = nome + ":" + str(alunos[nome]) + "\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


def carregar_dados():
    try:
        # Corrigido: usando with e melhorando o parser das notas
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()  # remove espaços e quebras de linha
                if ":" in linha:
                    partes = linha.split(":")
                    nome = partes[0]
                    # Corrigido: convertendo a string de notas para lista de números
                    notas_str = partes[1].replace("[", "").replace("]", "").replace(" ", "")
                    if notas_str:  # se não estiver vazio
                        notas = [float(nota) for nota in notas_str.split(",")]
                    else:
                        notas = []
                    alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Começando com lista vazia.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")


def menu():
    while True:
        print("\n" + "="*10 + " MENU " + "="*10)
        print("1 - Adicionar aluno")
        print("2 - Adicionar nota")
        print("3 - Mostrar alunos")
        print("4 - Remover aluno")
        print("5 - Salvar dados")
        print("6 - Carregar dados")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        # Corrigido: comparando com strings (input sempre retorna string)
        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            if nome:  # verifica se não está vazio
                adicionar_aluno(nome)
            else:
                print("Nome não pode estar vazio!")
                
        elif opcao == "2":
            nome = input("Nome: ").strip()
            if nome in alunos:
                try:
                    # Corrigido: convertendo para float
                    nota = float(input("Nota: "))
                    adicionar_nota(nome, nota)
                except ValueError:
                    print("Por favor, digite um número válido para a nota!")
            else:
                print("Aluno não encontrado!")
                
        elif opcao == "3":
            mostrar_alunos()
            
        elif opcao == "4":
            nome = input("Nome: ").strip()
            remover_aluno(nome)
            
        elif opcao == "5":
            salvar_dados()
            
        elif opcao == "6":
            carregar_dados()
            
        elif opcao == "7":
            print("Saindo do programa... Até logo!")
            break
            
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 7.")


# Inicia o programa
menu()
