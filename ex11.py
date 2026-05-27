# Desenvolva Cód. que digite um nome de usuario. Se o nome for "SENAC", imprimir "seja bem vindo Senac", senão imprimir "Usuario (nome_de_entrada) não cadastrado"

nome = input("Digite um nome: ").lower()
if nome == "SENAC" :
    print(f"Seja bem vindo {nome}")
else :
    print(f"Usuário {nome} não cadastrado")


# Com OR 
#nome = input("Digite seu nome: ")
#if nome == "SENAC" or "Senac" or "senac":
#    print(f"Seja bem vindo {nome}")
#else:
#    print(f"Usuário {nome} não cadastrado")


#Com ELIF
#nome = input("Digite seu nome: ")
#if nome == "SENAC" :
#    print(f"Seja bem vindo {nome}")
#elif nome == "Senac" :
#    print(f"Seja bem vindo {nome}")
#elif nome == "senac" :
#    print(f"Seja bem vindo {nome}")

#else:
#    print(f"Usuário {nome} não cadastrado")