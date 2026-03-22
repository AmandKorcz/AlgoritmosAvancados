def dois_melhores_tempos(tempos):
    if len(tempos) < 2:
        return None, None
    
    if tempos[0] < tempos[1]:
        primeiro = tempos[0]
        segundo = tempos[1]
    else:
        primeiro = tempos[1]
        segundo = tempos[0]

    for i in range(2, len(tempos)):
        tempo = tempos[i]

        if tempo < primeiro:
            segundo = primeiro
            primeiro = tempo
        elif tempo < segundo:
            segundo = tempo

    return primeiro, segundo

tempos = [58, 64, 55, 57, 60, 59]
primeiro, segundo = dois_melhores_tempos(tempos)

if primeiro is not None:
    print("Primeiro lugar: ", primeiro)
    print("Segundo lugar: ", segundo)
else:
    print("A lista não tem dois tempos registrados")
