def maior_temperatura(temperaturas):
    if len(temperaturas) == 0:
        return None
    
    maior = temperaturas[0]

    for temperatura in temperaturas:
        if temperatura > maior:
            maior = temperatura

    return maior

temperaturas = [31, 33, 27, 30, 28, 18, 45]

resultado = maior_temperatura(temperaturas)

if resultado is not None:
    print("A maior temperatura é: ", resultado)
else:   
    print("A lista de temperatura esta vazia")