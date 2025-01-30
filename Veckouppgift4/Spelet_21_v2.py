#Veckouppgift4_: Spelet_21_v2
#Funktionen skriver ut första slumpade tal mellan 1 -> 13 som är större än 21.
import random
def forsta_tal_store_an_21 ():
    total_sum = 0

    while True: #Loopen fortsätter tills summan överstiger 21.Varje iteration lägger till det aktuella talet (number) till total_sum
        card = random.randint(1,13)  # Slumpa ett tal mellan 1 och 13
        total_sum= total_sum + card
        print(f"Slumpat tal:{card}, summa: {total_sum}") # Skriv ut för att följa processen
        if total_sum > 21:                   #Om total_sum blir större än 21, returneras det aktuella talet (number)
            return card

# Anropa funktionen och skriv ut resultatet
forsta_store_tal = forsta_tal_store_an_21()
print("Det första slumpade talet som gör summa större än 21 är: ",forsta_store_tal)
