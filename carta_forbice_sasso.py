import random

continuare = True
lista_valori = ["carta", "forbice", "sasso"]
vittorie = 0
pareggi = 0
sconfitte = 0


def sconfitta(risultato):
    global sconfitte
    #global risultato, sconfitte
    print("È uscito", risultato, "\nHai perso!")
    sconfitte = sconfitte + 1


def vittoria(risultato):
    global vittorie
    print("È uscito", risultato, "\nHai vinto!")
    vittorie = vittorie + 1


def continuare_a_giocare():
    global continuare
    rigiocare = input("Vuoi continuare? (si o no): ")
    if (rigiocare == "no"):
        continuare = False


def stampa_risultati(pareggi, vittorie, sconfitte):
    print(f"\nRisultato finale:\nPareggi {pareggi} - Sconfitte {sconfitte} - Vittorie {vittorie}")
    if (vittorie > sconfitte):
        print("Hai vinto il gioco! :)")
    elif (vittorie == sconfitte):
        print("Pareggio :|")
    elif (vittorie <= sconfitte):
        print("Non hai vinto il gioco :(")


def cartaForbiceSasso():
    global risultato, pareggi, sconfitte, vittorie
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
                    sconfitta(risultato)
                    continuare_a_giocare()
                else:
                    vittoria(risultato)
                    continuare_a_giocare()
            elif risultato == "forbice":
                if tiro == "sasso":
                    vittoria(risultato)
                    continuare_a_giocare()
                else:
                    sconfitta(risultato)
                    continuare_a_giocare()
            elif risultato == "sasso":
                if tiro == "forbice":
                    sconfitta(risultato)
                    continuare_a_giocare()
                else:
                    vittoria(risultato)
                    continuare_a_giocare()
    stampa_risultati(pareggi, vittorie, sconfitte)


cartaForbiceSasso()
