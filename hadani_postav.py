# HRA - HÁDÁNÍ POSTAV

import random

seznam_postav = ("Harry", "Hermiona", "Ron", "Draco", "Albus")
hadana_postava = seznam_postav[random.randint(0, len(seznam_postav) -1)]
tip_hrace = ""
pocet_pokusu = 0
cara = "-" * 40

print(f"\nVítejte v naší hádací hře!\n{cara}\nMáte tři pokusy, abyste uhodli jmého postavy z Harryho Pottera z tohoto seznamu:\n", ", ".join(seznam_postav))

while tip_hrace != hadana_postava:
    if pocet_pokusu < 3:
        tip_hrace = input("Zadejte jméno postavy:\n")
        pocet_pokusu += 1
    else:
        print("Počet pokusů byl bohužel vyčerpán.")
        break

    if tip_hrace == hadana_postava:
        print(f"Uhádli jste, hádaná postava byla {hadana_postava}. Gralujuji!")

