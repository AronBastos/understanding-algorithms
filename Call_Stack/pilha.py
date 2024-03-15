def sauda(nome):
    print("Ola, " + nome + "!")
    sauda2(nome)
    print("Preparando para dizer tchau...")
    tchau()

def sauda2(nome):
    print("Ola de novo, " + nome + "!")

def tchau():
    print("Tchau!")

# Agora podemos chamar a função sauda com um nome
sauda("Usuario")
