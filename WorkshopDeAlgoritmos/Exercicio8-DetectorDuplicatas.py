def existe_duplicatas(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

sequencia = [130, 324, 255, 132, 888, 130]

if existe_duplicatas(sequencia):
    print("Existem valores repetidos na lista")
else:
    print("Não existem valores repetidos na lista")