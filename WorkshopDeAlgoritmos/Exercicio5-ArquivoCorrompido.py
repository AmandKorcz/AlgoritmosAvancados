def busca_binaria(nomes, nome_procurado):
    inicio = 0
    fim = len(nomes) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if nomes[meio] == nome_procurado:
            return meio
        elif nome_procurado < nomes[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

usuarios = ['Amanda', 'Bruna', 'Carol', 'Daniela', 'Eduarda', 'Fernanda']
nome = input("Digite o nome que vamos procurar: ")

resultado = busca_binaria(usuarios, nome)

if resultado != -1:
    print(f"{nome} foi encontrado na posição {resultado}")
else:
    print(f"{nome} não foi encontrado na lista")