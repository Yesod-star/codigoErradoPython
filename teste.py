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
        # ❌ ERRO ORIGINAL: "if nota < 0 a   'nd nota > 10:"
        if nota < 0 or nota > 10:  # ✅ Correção: troca de "a 'nd" por "or"
            print("Nota inválida!")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        soma = 0
        for n in notas:
            soma += n  # ✅ Correção: antes era "soma = n" (sobrescrevia o valor)
        if len(notas) == 0:  # ✅ Correção: evita divisão por zero
            print("Aluno não possui notas cadastradas.")
            return None
        media = soma / len(notas)
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    if len(alunos) == 0:  # ✅ Correção: moveu verificação para o início
        print("Nenhum aluno cadastrado!")
        return

    print("===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        print("Nome:", aluno)
        print("Notas:", alunos[aluno])
        media = calcular_media(aluno)
        print("Média:", media if media is not None else "-")  # ✅ Evita erro com None
        print("----------------------")


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
    else:
        print("Aluno não existe")
    # print("Remoção concluída!")  # ❌ Removido: mostrava mensagem mesmo com erro


def salvar_dados():
    # ❌ ERRO ORIGINAL: arquivo aberto sem fechamento
    with open("alunos.txt", "w") as arquivo:  # ✅ Correção: usa with para fechar automaticamente
        for nome in alunos:
            linha = nome + ":" + ",".join(map(str, alunos[nome])) + "\n"  # ✅ Corrige formato da lista
            arquivo.write(linha)
    print("Dados salvos com sucesso!")  # ✅ Feedback adicionado


def carregar_dados():
    try:
        with open("alunos.txt") as arquivo:  # ✅ Correção: uso de with e leitura adequada
            for linha in arquivo.readlines():
                partes = linha.strip().split(":")
                nome = partes[0]
                # ❌ ERRO ORIGINAL: partes[1].split(",") dava erro com formato "[1, 2, 3]"
                notas = [float(n) for n in partes[1].split(",") if n]  # ✅ Converte corretamente
                alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except FileNotFoundError:  # ✅ Correção: tratamento específico
        print("Arquivo não encontrado. Nenhum dado carregado.")
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

        # ❌ ERRO ORIGINAL: comparava com número inteiro (input é string)
        if opcao == "1":  # ✅ Correção: comparação feita como string
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == "2":
            nome = input("Nome: ")
            try:
                nota = float(input("Nota: "))  # ✅ Correção: converte input para número
                adicionar_nota(nome, nota)
            except ValueError:
                print("Nota inválida, insira um número.")
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


menu()  # ✅ Correção: apenas chamada direta da função, removido texto extra no final
