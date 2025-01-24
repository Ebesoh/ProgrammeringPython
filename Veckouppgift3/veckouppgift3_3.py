#veckouppgift3_3
#Kvittouträknaren
#from Veckouppgift3.veckouppgift3_2 import total
from contextlib import nullcontext

print("Välkommen till Kvittokompis! Avsluta genom att skriva: 'quit' ")
belopp_lista = []
total_belopp = 0
belopp= ""
total_belopp_plus_dricks = 0

while belopp != "quit":
    belopp = input("Skriv in ett belopp:")
    if belopp.isdigit():                 # Checks if string contains a digit
        belopp_lista.append(belopp)      # Appends the digit(s) to the list( belopp_lista)
    elif belopp == "quit":               # Exits program if user inputs 'quit'
        break
    else:
        continue
print("Inskrivna belopp är: ",belopp_lista)
total_Int_belopp = [int(x) for x in belopp_lista]  # Converts all string list to integers
total_belopp = sum(total_Int_belopp)               # Sum all integers in the list
print("Det blir",total_belopp,"kr totalt. Välkommen åter")

# Version 2 code
person_i_sallskapet= input("Hur många är ni?:")
belopp_per_person = total_belopp / int(person_i_sallskapet)
print("Det blir",total_belopp,"kr totalt, alltså",float(belopp_per_person),"kr per person. Välkommen åter")


# Version 3 code
dricks = (input("Hur många procent dricks vill ni lägga?:"))
if dricks == "":
    print(total_belopp)
    total_belopp_plus_dricks = total_belopp * (100 + 10)/100
    print("Total belopp plus dricks 10% bli: ", total_belopp_plus_dricks)
else:
    total_belopp_plus_dricks = total_belopp * (100 + int(dricks))/100
    print("Total belopp plus inmatade dricks bli:", total_belopp_plus_dricks,"kr. Välkommen åter")


