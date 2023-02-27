# Hra kostky...
import random

jedna = '''  
        ┌─────────┐ 
        │         │ 
        │    ●    │ 
        │         │  
        └─────────┘
'''
dva = '''
        ┌─────────┐
        │    ●    │
        │         │
        │    ●    │
        └─────────┘
'''
tri = '''
        ┌─────────┐
        │ ●       │
        │    ●    │
        │       ● │
        └─────────┘
'''
ctyri = '''
        ┌─────────┐
        │ ●     ● │
        │         │
        │ ●     ● │
        └─────────┘ 
'''
pet = '''
        ┌─────────┐
        │ ●     ● │
        │    ●    │
        │ ●     ● │
        └─────────┘  
'''
sest = '''
        ┌─────────┐
        │ ●     ● │
        │ ●     ● │
        │ ●     ● │
        └─────────┘
'''


hody_kostkou = (jedna, dva, tri, ctyri, pet, sest)

print("\nCHCEŠ SI HÁRAT? :)))\nSuper, pojďmě si zahrát KOSTKY!\n")
hod_hrace = input("Pro hození kostkou zmáčkni ENTER:\n")

if len(hod_hrace) == 0:
    hod_hrace = random.randint(1,6)
    hod_pc = random.randint(1,6)
    print(f"TVŮJ HOD:\n{hody_kostkou[(hod_hrace) -1]}")
    print(f"MŮJ HOD:\n{hody_kostkou[(hod_pc) -1]}")
    if hod_hrace > hod_pc:
        print("---> VYHRÁVÁŠ! Gratuluji... =)\n")
    elif hod_hrace < hod_pc:
        print("---> PROHRÁVÁŠ... =(\n")
    elif hod_hrace == hod_pc:
        print("---> REMÍZA... Zkusíme to znovu?\n")
else:
    print("Neplatná volba. Ukončuji...")