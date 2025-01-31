#Spel_datorn_användare
####################################################################
# Koden implementerar ett enkelt spel "21", även känt som Blackjack.
# Spelaren tävlar mot datorn för att få ett totalt kortvärde så nära 21 som möjligt utan att överskrida det
#############################################################################################################
import  random

#funktion som slumpmässigt drar tal mellan 1 och 13 tills summan överstiger 21
def sum_over_21():
    total = 0
    while total <= 21:
        kort =random.randint(1,13)
        total = total + kort
        print(f"Du drog: {kort}, totalen är nu: {total}")
    print(f"Summan blev: {total}, vilket är större än 21.")
sum_over_21()

def play_21():
    anvandare_total = 0
    datorn_total = 0

    # Spelaren tar kort
    while True:
        kort = input("Vill du ta ett nytt kort (ja/nej)? ").lower() # lower() method används för att säkerställa input är alltid small bokstav
        if kort == "ja":
            card = random.randint(1, 13)
            anvandare_total =anvandare_total + kort
            print(f"Du drog: {kort}, din total är nu: {anvandare_total}")
            if anvandare_total > 21:
                print("Du gick över 21! Du förlorade.")
                return
        else:
            print(f"Du stannar med totalen: {anvandare_total}")
            break

    # Datorn tar kort
    while datorn_total < 17:  # Datorn stannar när den når 17 eller högre, datorn simulerade motståndare
    #while True:
        kort = random.randint(1, 13)
        datorn_total = datorn_total + kort
        print(f"Datorn drog: {kort}, datorns total är nu: {datorn_total}")
        if datorn_total > 21:
            print("Datorn gick över 21! Du vann.")
            return

    # Jämför totalsummorna för att avgöra vem som har vunnit
    if anvandare_total > datorn_total:
        print(f"Du vann! Din total: {anvandare_total}, datorns total: {datorn_total}")
    elif anvandare_total < datorn_total:
        print(f"Datorn vann! Datorns total: {datorn_total}, din total: {anvandare_total}")
    else:
        print(f"Det blev oavgjort! Både du och datorn har {anvandare_total}.")

# Anropa funktionen
play_21()

