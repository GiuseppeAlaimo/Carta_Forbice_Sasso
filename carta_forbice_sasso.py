import random
continuare = True


def continuare_a_giocare():
    global continuare
    rigiocare = input("Vuoi continuare? (si o no): ")
    if (rigiocare == "no"):
        continuare = False
    return continuare


def cartaForbiceSasso():
    lista_valori = ["carta", "forbice", "sasso"]
    vittorie = 0
    pareggi = 0
    sconfitte = 0
    print("Iniziamo!")

    while continuare:
        tiro = input("Carta Forbice o Sasso? Cosa scegli? ").lower()
        if tiro not in lista_valori:
            print("Scelta non valida, riprova")
        else:
            risultato = random.choice(lista_valori)
            if risultato == tiro:
                print("È uscito", risultato, "\nPareggio")
                pareggi = pareggi + 1
                continuare_a_giocare()
            elif risultato == "carta":
                if tiro == "sasso":
                    print("È uscito", risultato, "\nHai perso!")
                    sconfitte = sconfitte + 1
                    continuare_a_giocare()
                else:
                    print("È uscito", risultato, "\nHai vinto!")
                    vittorie = vittorie + 1
                    continuare_a_giocare()
            elif risultato == "forbice":
                if tiro == "sasso":
                    print("È uscito", risultato, "\nHai vinto!")
                    vittorie = vittorie + 1
                    continuare_a_giocare()
                else:
                    print("È uscito", risultato, "\nHai perso!")
                    sconfitte = sconfitte + 1
                    continuare_a_giocare()
            elif risultato == "sasso":
                if tiro == "forbice":
                    print("È uscito", risultato, "\nHai perso!")
                    sconfitte = sconfitte + 1
                    continuare_a_giocare()
                else:
                    print("È uscito", risultato, "\nHai vinto!")
                    vittorie = vittorie + 1
                    continuare_a_giocare()
    print(
        f"\nRisultato finale:\nPareggi {pareggi} - Sconfitte {sconfitte} - Vittorie {vittorie}")
    if (vittorie > sconfitte):
        print("Hai vinto il gioco! :)")
    elif (vittorie == sconfitte):
        print("Pareggio :|")
    elif (vittorie <= sconfitte):
        print("Non hai vinto il gioco :(")


cartaForbiceSasso()
