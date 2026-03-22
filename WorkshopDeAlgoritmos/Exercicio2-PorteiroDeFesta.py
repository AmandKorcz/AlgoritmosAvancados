def busca_linear(convidados, nome_procurado):
    for nome in convidados:
        if nome == nome_procurado:
            return True
    return False
    
lista_convidados = ["Amanda", "Flavia", "Guilherme", "Gustavo", "Pedro"]
nome = input("Digite o nome que deseja procurar: ")

if busca_linear(lista_convidados, nome):
    print(f"{nome} está na lista de convidados")
else:
    print(f"{nome} não está na lista de convidados")