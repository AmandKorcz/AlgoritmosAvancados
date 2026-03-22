def dois_maiores(valores):
    if len(valores) < 2:
        print("A lista precisa de pelo menos dois valores")
        return
    
    if valores[0] > valores[1]:
        maior = valores[0]
        segundo = valores[1]
    else:
        maior = valores[1]
        segundo = valores[0]

    comparacoes = 1

    for i in range(2, len(valores)):
        comparacoes += 1
        if valores[i] > maior:
            segundo = maior
            maior = valores[i]
        else:
            comparacoes += 1
            if valores[i] > segundo:
                segundo = valores[i]

    print("Maior valor = ", maior)
    print("Segundo maior valor = ", segundo)
    print("Comparações: ", comparacoes)

lista = [10, 5, 8, 20, 28, 3, 9]
dois_maiores(lista)
