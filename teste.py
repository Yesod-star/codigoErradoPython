import ast

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
        if nota < 0 or nota > 10:  # ✅ aparentemente esse era mais facil, possivelmene agora deu certo
            print("Nota inválida!")
        else:
            alunos[nome].append(nota)
            print("Nota adicionada com sucesso!")


def calcular_media(nome):
    if nome in alunos:
        notas = alunos[nome]
        soma = 0
        for n in notas:
            soma += n  # ✅ sobrescreve em vez de somar
        if not notas:
            print("Aluno não tem notas")
            return None
        media = soma / len(notas)  # ✅ sé pa isso não ta funcionando 
        return media
    else:
        print("Aluno não existe")
        return None


def mostrar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!") # ✅ agora vai
        return
    
    print("===== LISTA DE ALUNOS =====")
    for aluno in alunos:
        print("Nome:", aluno)
        print("Notas:", alunos[aluno])
        media = calcular_media(aluno)
        print("Média:", "Sem notas cadastradas" if media is None else media)  # ✅ agora vai profavelmente dar certo chefia
        print("----------------------")


def remover_aluno(nome):
    if nome in alunos:
        alunos.pop(nome)
        print("Aluno removido com sucesso")
        print("Remoção concluída!")  # ✅ agpra vai mostrar normlmente, melzinho na chupeta
    else:
        print("Aluno não existe")


def salvar_dados():
    arquivo = open("alunos.txt", "w")
    for nome in alunos:
        linha = nome + ":" + str(alunos[nome]) + "\n"
        arquivo.write(linha)
    arquivo.close() # ✅ agora vai


def carregar_dados():
    try:
        arquivo = open("alunos.txt")
        for linha in arquivo.readlines():
            partes = linha.split(":")
            nome = partes[0]
            raw = partes[1].strip()
            try:
                notas = ast.literal_eval(raw)
                if not isinstance(notas, list):
                    notas = []
            except Exception:
                notas = []
            alunos[nome] = notas
        print("Dados carregados com sucesso!")
    except:
        print("Erro ao carregar dados! Verifique se o arquivo existe e está no formato correto.")  # ✅ tratamento nada generico
    finally: # ✅ agora vai
        arquivo.close()

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

        opcao = int(input("Escolha: "))

        if opcao == 1:  # ✅ Resolvido, era so ter colocado int antes do input
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)
        elif opcao == 2:
            nome = input("Nome: ")
            nota = int(input("Nota: "))  # ✅ pronto papai, agora ele pega numeros
            adicionar_nota(nome, nota)
        elif opcao == 3:
            mostrar_alunos()
        elif opcao == 4:
            nome = input("Nome: ")
            remover_aluno(nome)
        elif opcao == 5:
            salvar_dados()
        elif opcao == 6:
            carregar_dados()
        elif opcao == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
 
