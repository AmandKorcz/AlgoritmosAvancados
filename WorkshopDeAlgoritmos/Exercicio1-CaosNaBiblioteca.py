def bubble_sort(livros):
    n = len(livros)

    for i in range(n):
        trocou = False

        for j in range(0, n-1-i):
            if livros[j] > livros[j+1]:
                livros[j], livros[j+1] = livros[j+1], livros[j]
                trocou = True

        if not trocou:
            print("Lista ordenada")
            break

    return livros

livros = [5, 2, 4, 1, 3]
resultado = bubble_sort(livros)

print("Livros ordenados: ", resultado)