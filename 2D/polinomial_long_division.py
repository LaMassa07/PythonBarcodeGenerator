from log import log2
from power_of_two import generate_power_of_two

#inserire con il grado massimo a sinistra e il minimo a destra
def division(messaggio, generatore):
    parziale = messaggio

    risultato = []

    #lunghezza_risultato = len(messaggio) - len(generatore) + 1

    for j in range(0, len(messaggio) - len(generatore) + 1):
        n = parziale[j] // generatore[0]

        risultato.append(n)

        new_parziale = []
        for i in range(j):
            new_parziale.append(0)
        for i in range(0, len(generatore)):
            new_parziale.append(n*generatore[i])

        temp = []
        for i in range(0, len(new_parziale)):
            temp.append(parziale[i] - new_parziale[i])


        parziale = temp
        try:
            parziale.append(messaggio[j + len(generatore)])
        except IndexError:
            pass

    return parziale


#print(division([250, 246, 245, 23, 1], [23, 34, 34]))