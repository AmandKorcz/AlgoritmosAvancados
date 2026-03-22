def jogo_adivinhacao():
    inicio = 1
    fim = 100
    tentativas = 0

    print("Pense em um número de 1 a 100")
    print("Responda apenas com: ")
    print("'sim' se o número sugerido estiver correto")
    print("'maior' se o número for maior que o número sugerido")
    print("'menor' se o número for menor que o número sugerido")
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        tentativas += 1

        print(f"\nTentativa {tentativas}")
        print(f"O número é {meio}?")
        resposta = input().strip().lower()

        if resposta == "sim":
            print(f"O núnero {meio} foi descoberto em {tentativas} tentativas")
            return
        elif resposta == "maior":
            inicio = meio + 1
        elif resposta == "menor":
            fim = meio - 1
        else:
            print("Resposta inválida. Esperado apenas 'maior', 'menor' e 'sim'")

        print("Resposta inválida")

jogo_adivinhacao() 