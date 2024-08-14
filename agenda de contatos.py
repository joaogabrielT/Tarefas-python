agenda = []
# Variável para marcar uma alteração na agenda
alterada = False

# Solicita ao usuário um nome. Se o usuário não fornecer um nome, utiliza o valor padrão fornecido
def pede_nome(padrão=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome

# Solicita ao usuário um telefone. Se o usuário não fornecer um telefone, utiliza o valor padrão fornecido
def pede_telefone(padrão=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

# Solicita ao usuário um endereço. Se o usuário não fornecer um endereço, utiliza o valor padrão fornecido
def pede_endereço(padrão=""):
    endereço = input("Endereço: ")
    if endereço == "":
        endereço = padrão
    return endereço

# Solicita ao usuário uma cidade. Se o usuário não fornecer uma cidade, utiliza o valor padrão fornecido
def pede_cidade(padrão=""):
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrão
    return cidade

# Solicita ao usuário uma UF. Se o usuário não fornecer uma UF, utiliza o valor padrão fornecido
def pede_uf(padrão=""):
    uf = input("UF: ")
    if uf == "":
        uf = padrão
    return uf

# Exibe os dados completos de um contato
def mostra_dados(nome, telefone, endereço, cidade, uf):
    print(f"Nome: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereço}")
    print(f"Cidade: {cidade}")
    print(f"UF: {uf}")

# Solicita ao usuário o nome de um arquivo
def pede_nome_arquivo():
    return input("Nome do arquivo: ")

# Procura um contato na agenda pelo nome. Retorna o índice do contato se encontrado, ou None se não encontrado
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

# Adiciona um novo contato à agenda. Solicita nome, telefone, endereço, cidade e UF, e marca a agenda como alterada.
def novo():
    global agenda, alterada
    nome = pede_nome()
    telefone = pede_telefone()
    endereço = pede_endereço()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, endereço, cidade, uf])
    alterada = True

# Solicita confirmação para realizar uma operação (S/N). Repete até receber uma resposta válida.
def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

# Remove um contato da agenda
def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

# Altera os dados de um contato existente
def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome, telefone, endereço, cidade, uf = agenda[p]
        print("Encontrado:")
        mostra_dados(nome, telefone, endereço, cidade, uf)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor atual
        telefone = pede_telefone(telefone)
        endereço = pede_endereço(endereço)
        cidade = pede_cidade(cidade)
        uf = pede_uf(uf)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, endereço, cidade, uf]
            alterada = True
    else:
        print("Nome não encontrado.")

# Lista todos os contatos na agenda com suas posições e dados
def lista():
    print("\nAgenda\n\n\------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("\------\n")

# Lê o nome do último arquivo de agenda gravado e carrega os dados desse arquivo
def lê_última_agenda_gravada():
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

# Obtém o nome do último arquivo de agenda a partir do arquivo "ultima agenda.dat"
def última_agenda():
    try:
        arquivo = open("ultima agenda.dat", "r", encoding="utf-8")
        última = arquivo.readline().strip()
        arquivo.close()
    except FileNotFoundError:
        return None
    return última

# Atualiza o arquivo "ultima agenda.dat" com o nome do arquivo da agenda mais recente
def atualiza_última(nome):
    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

# Lê os dados de um arquivo de agenda e atualiza a lista agenda. Cada linha do arquivo deve estar no formato "nome#telefone#endereço#cidade#uf".
def leia_arquivo(nome_arquivo):
    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone, endereço, cidade, uf = l.strip().split("#")
            agenda.append([nome, telefone, endereço, cidade, uf])
    alterada = False

# Pergunta ao usuário se deseja gravar a agenda se houver alterações não salvas
def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)

# Ordena a lista de contatos por nome
def ordena():
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i][0] > agenda[i + 1][0]:  # Compara nomes
                # Troca os contatos
                agenda[i], agenda[i + 1] = agenda[i + 1], agenda[i]
                trocou = True
            i += 1
        if not trocou:
            break
    alterada = True

# Grava a lista de contatos em um arquivo
def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n\------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
    atualiza_última(nome_arquivo)
    alterada = False

# Valida se um valor está dentro de um intervalo definido
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

# Exibe o menu de opções e solicita ao usuário que escolha uma opção
def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

# Lê o último arquivo de agenda gravado e inicia o loop do menu principal.
lê_última_agenda_gravada()
while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        ordena()