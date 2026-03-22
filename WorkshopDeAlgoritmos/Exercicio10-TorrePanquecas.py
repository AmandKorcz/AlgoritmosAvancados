def flip(pilha, k):
    inicio = 0
    while inicio < k:
        pilha[inicio], pilha[k] = pilha[k], pilha[inicio]
        inicio += 1
        k -= 1

def encontrar_indice_maior(pilha, tamanho):
    indice_maior = 0
    for i in range(1, tamanho):
        if pilha[i] > pilha[indice_maior]:
            indice_maior = i
    return indice_maior

def pancake_sort(pilha):
    n = len(pilha)

    for tamanho_atual in range(n, 1, -1):
        indice_maior = encontrar_indice_maior(pilha, tamanho_atual)

        if indice_maior == tamanho_atual - 1:
            continue

        if indice_maior != 0:
            flip(pilha, indice_maior)
            print(f"Flip até a posção {indice_maior}: {pilha}")

        flip(pilha, tamanho_atual - 1)
        print(f"Flip até a posição {tamanho_atual - 1}: {pilha}")

    return pilha

panquecas = [3, 6, 1, 5, 2, 4]
print("Pilha incial: ", panquecas)

resultado = pancake_sort(panquecas)

print("Pilha ordenada: ", resultado)