# HRA: UHODNI ČÍSLO

import random
import os

# PROMĚNNÉ
logo = """
 _____   ____  _____             ______    _____   _____ 
|  __ \ / __ \|  __ \     /\    |___  /   |  __ \ / ____|
| |__) | |  | | |__) |   /  \      / /    | |__) | |     
|  ___/| |  | |  _  /   / /\ \    / /     |  ___/| |     
| |    | |__| | | \ \  / ____ \  / /__    | |    | |____ 
|_|     \____/|_|  \_\/_/    \_\/_____|   |_|     \_____|
"""

oddelovac1 = "-" * 50
oddelovac2 = "=" * 58
obtiznost = ("easy", "hard")
pocet_pokusu = 0
monosti_pokracovani = ("ano", "ne")
skore_pc_hrac = [0, 0]
repete = True

# VLASTNÍ KÓD
print(f"{logo}\n{oddelovac2}\n\nVítej v naší hádací hře!\n"
      "Dokážeš porazit počítač? Uhodni číslo od 1 do 100 a vyhraješ!")

while repete:
    
    # VOLBA OBTÍŽNOSTI
    zvolena_obtiznost = input("Zvol si obtížnost hry ('easy' = lehka; 'hard' = tězka): ")
    zvolena_obtiznost = zvolena_obtiznost.lower()
    
    if zvolena_obtiznost not in obtiznost:
        print("Neplatná volba, zkus to znovu...")
        continue
    else:
        if zvolena_obtiznost == "easy":
            pocet_pokusu = 10
        elif zvolena_obtiznost == "hard":
            pocet_pokusu = 5

    # HÁDÁNÍ ČÍSLA
    hadane_cislo = random.randint(1, 100)

    while not pocet_pokusu == 0:
        zadane_cislo = (input("Zadej číslo: "))
        if zadane_cislo.isnumeric():
            zadane_cislo = int(zadane_cislo)
            if zadane_cislo == hadane_cislo:
                skore_pc_hrac[1] += 1
                print(f"\nAno! Hádané číslo bylo {hadane_cislo}. Tohle kolo jsi VYHRÁL!"
                    f":)\n{oddelovac1}")
                break
            elif zadane_cislo < hadane_cislo:
                pocet_pokusu -= 1
                print(f"Příliš nízké číslo. Počet zbývajících pokusů: {pocet_pokusu}")
            elif zadane_cislo > hadane_cislo:
                pocet_pokusu -= 1
                print(f"Příliš vysoké číslo. Počet zbývajících pokusů: {pocet_pokusu}")
        else:
            print("Neplatná volba, zkus to znovu...")

    if pocet_pokusu == 0:
        print("\nBohužel jsi číslo neuhádl, mělo to být "
              f"číslo {hadane_cislo}.\n{oddelovac1}")
        skore_pc_hrac[0] += 1
        
    # MOŽNOST POKRAČOVÁNÍ
    while True:
        pokracovani = input("Chceš ve hře pokračovat? ('ano' / 'ne'): ")
        if pokracovani not in monosti_pokracovani:
            print("Neplatná volba, zkus to znovu...")
        elif pokracovani == "ano":
            os.system("cls")
            print(logo)
            break
        elif pokracovani == "ne":
            repete = False
            break

# VÝPIS VÝSLEDKŮ    
print(f"\nCelkové skóre je: POČÍTAČ {skore_pc_hrac[0]} | HRÁČ {skore_pc_hrac[1]}")
if skore_pc_hrac[0] > skore_pc_hrac[1]:
    print(f"\nJe mi líto, dnes vyhrává počítač... :(\n{oddelovac2}")
elif skore_pc_hrac[0] < skore_pc_hrac[1]:
    print(f"\nGratuluju, PORAZIL JSI POČÍTAČ! :)\n{oddelovac2}")
elif skore_pc_hrac[0] == skore_pc_hrac[1]:
    print(f"\nBylo to napínavé a výsledek je REMÍZA!\n{oddelovac2}")