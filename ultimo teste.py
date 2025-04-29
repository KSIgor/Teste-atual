print("Bem vindos, aqui vocês irão ver sua turma.\n")
print("Para começar digite seu nome.\n")


def primeiro_nome_fun():
    global primeiro_nome
    primeiro_nome = input("Qual é o seu primeiro nome?\n").capitalize()
    print(f"Seu primeiro nome é: {primeiro_nome}?\n")
    resposta_1 = input("SIM ou NÃO?\n").capitalize()
    while primeiro_nome == primeiro_nome:
        if resposta_1 == "Sim":
            break
        elif resposta_1 == "Não":
            primeiro_nome = input("Qual é o seu primeiro nome?\n").capitalize()
            print(f"Seu primeiro nome é: {primeiro_nome}?\n")
            resposta_1 = input("SIM ou NÃO?\n").capitalize()
        elif resposta_1 == "Nao":
            primeiro_nome = input("Qual é o seu primeiro nome?\n").capitalize()
            print(f"Seu primeiro nome é: {primeiro_nome}?\n")
            resposta_1 = input("SIM ou NÃO?\n").capitalize()
        else:
            print("Digite uma opção válida:\n")
            primeiro_nome = input("Qual é o seu primeiro nome?\n").capitalize()
            print(f"Seu primeiro nome é: {primeiro_nome}?\n")
            resposta_1 = input("SIM ou NÃO?\n").capitalize()

primeiro_nome_fun()

def sobrenome_completo_fun():
    global sobrenome_completo
    print("Agora digite seu sobrenome completo.\n")
    sobrenome_completo = input("Qual o seu sobrenome completo?\n").title()
    print(f"Seu sobrenome é: {sobrenome_completo}?\n")
    resposta_2 = input("SIM ou NÃO?").capitalize()
    while sobrenome_completo == sobrenome_completo:
        if resposta_2 == "Sim":
            break
        elif resposta_2 == "Não":
            sobrenome_completo = input("Digite o seu sobrenome completo?\n").title()
            print(f"Seu sobrenome é: {sobrenome_completo}?\n")
            resposta_2 = input("SIM ou NÃO?").capitalize()
        elif resposta_2 == "Nao":
            sobrenome_completo = input("Digite o seu sobrenome completo?\n").title()
            print(f"Seu sobrenome é: {sobrenome_completo}?\n")
            resposta_2 = input("SIM ou NÃO?").capitalize()
        else:
            print("Digite uma opção válida:\n")
            sobrenome_completo = input("Qual o seu sobrenome completo?\n").title()
            print(f"Seu sobrenome é: {sobrenome_completo}?\n")
            resposta_2 = input("SIM ou NÃO?").capitalize()

sobrenome_completo_fun()

nome_completo = primeiro_nome + " " + sobrenome_completo
def idade_fun():
    global idade_correta
    idade_correta = int(input(f"Certo {primeiro_nome}, informe qual a sua idade.\n"))
    while idade_correta == idade_correta:
        if idade_correta >=18:
            resposta_3 = input("Sua idade está correta? SIM ou NÃO?").capitalize()
            if resposta_3 == "Sim":
                    break
            elif resposta_3 == "Não":
                    input("Digite sua idade correta:")
            elif resposta_3 == "Nao":
                    input("Digite sua idade correta:")     
        elif idade_correta <=17:
            print("Você não tem permissão para este serviço")
            idade_correta = int(input("Digite uma idade coerente:"))
        elif idade_correta >= 90:
            print("Você ultrapassou a idade necessária, por favor, digitar uma idade verídica:")
            idade_correta = int(input("Qual a sua idade?"))
idade_fun()

genero = input("E seu gênero?\n").capitalize()
while genero == genero:
    if genero == "Masculino":
        genero = "Masculino"
        break
    elif genero == "Feminino":
        genero = "Feminino"
        break
    else:
        print("Digite um gênero válido:")
    genero = input("E seu gênero?\n")

if genero == "MASCULINO":
    alunos_1 = [primeiro_nome,"Livia","Marcelle","Pablo","Leonora","Stefann"]
    print(f"Certo, {nome_completo}, vejamos sua sala: {alunos_1}\n")
    alunos_2 = ["Lucas","Gisele","Roberta","Pedro","Millene","Wagner"]
    print(f"Uma outra turma será adicionada em sua sala, confira: {alunos_2}\n")
    lista_de_alunos3 = alunos_1 + alunos_2
    print("Bom... Sua turma será composta por:\n")
    for alunos in lista_de_alunos3:
        print(alunos)
elif genero == "FEMININO":
    alunos_1 = [primeiro_nome.lower(),"Livia","Marcelle","Pablo","Leonora","Stefann"]
    print(f"Certo, {nome_completo}, vejamos sua sala: {alunos_1}\n")
    alunos_2 = ["Lucas","Gisele","Roberta","Pedro","Millene","Wagner"]
    print(f"Uma outra turma será adicionada em sua sala, confira: {alunos_2}\n")
    lista_de_alunos3 = alunos_1 + alunos_2
    print("Bom... Sua turma será composta por:\n")
    for alunos in lista_de_alunos3:
        print(alunos)