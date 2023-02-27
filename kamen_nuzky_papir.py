# HRA kámen nůžky papír

import random

kamen = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
nuzky = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

papir = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

obrazky = (kamen, nuzky, papir)
skore_hrac_pc = [0, 0]
oddelovac = "-" *40

print("\nCHCEŠ SI HÁRAT? :)))\n"
f"Super, zahrajme si Kámen, nůžky, papír!\n{oddelovac}\n")


while True:
    volba_hrac = input("Zadej číslo svojí volby:\n"
    "1 -> KÁMEN\n2 -> NŮŽKY\n3 -> PAPÍR\n4 -> UKONČENÍ HRY\n")

    if not volba_hrac.isdigit():
        print("Neplatná volba, zkus to znovu.")
    elif int(volba_hrac) >= 5:
        print("Neplatná volba, zkus to znovu.")
    elif int(volba_hrac) == 4:
        print("Konec hry... ")
        break
    else:
        volba_hrac = int(volba_hrac) 
        volba_pc = random.randint(0,2)
        obr_hrac = obrazky[int(volba_hrac) -1]
        obr_pc = obrazky[volba_pc]
        print(f"TVOJE VOLBA:\n{obr_hrac}")
        print(f"MOJE VOLBA:\n{obr_pc}")

        if volba_hrac == volba_pc:
            print("\n--- REMÍZA ---\n")
        elif volba_hrac == 1 and volba_pc == 2:
            print("Kámen tupí nůžky-->\n\n--> VYHRÁVÁŠ! =)\n")
            skore_hrac_pc[0] += 1
        elif volba_hrac == 1 and volba_pc == 3:
            print("Papír balí kámen-->\n\n--> PROHRÁVÁŠ =(\n")
            skore_hrac_pc[1] += 1
        elif volba_hrac == 2 and volba_pc == 1:
            print("Kámen tupí nůžky-->\n\n--> PROHRÁVÁŠ =(\n")
            skore_hrac_pc[1] += 1
        elif volba_hrac == 2 and volba_pc == 3:
            print("Nůžky stříhají papír-->\n\n--> VYHRÁVÁŠ! =)\n")
            skore_hrac_pc[0] += 1
        elif volba_hrac == 3 and volba_pc == 1:
            print("Papír balí kámen-->\n\n--> VYHRÁVÁŠ! =)\n")
            skore_hrac_pc[0] += 1
        elif volba_hrac == 3 and volba_pc == 2:
            print("Nůžky stříhají papír-->\n\n--> PROHRÁVÁŠ =(\n")
            skore_hrac_pc[1] += 1

print(f"Celkové skoré je:\nHRÁČ: {skore_hrac_pc[0]} | PC: {skore_hrac_pc[1]}")

if skore_hrac_pc[0] == skore_hrac_pc[1]:
    print("Souboj skončil remízou...")
elif skore_hrac_pc[0] > skore_hrac_pc[1]:
    print("Výhral jsi souboj s PC!")
elif skore_hrac_pc[0] < skore_hrac_pc[1]:
    print("V tomto souboji vyhrál PC :(.")