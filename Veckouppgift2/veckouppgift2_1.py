# 1. Vad är syftet med koden?
#Svar:
# 2. Testkör koden med några olika värden.
#Svar:
# 3. Finns det några direkta fel i koden? (fel som gör att programmet kraschar).
#Svar:
# 4. Finns det logiska fel? (programmet gör något annat än det är tänkt)
#Svar:
# 5. Diskutera möjliga lösningar på felen ni hittat.
#Svar:
# 6. Diskutera möjliga förbättringar på koden.
#Svar:
from operator import truediv

is_member = False
level1 = 100
level2 = 300
discount = 0

# Fel i koden eftersom om gränsvillkor uppfylla inte kravet. så länge price > level1 kommer alltid både level1&2 rabatter att exekvera och total skall 10% + 25%.
#print("\n***** Fel i koden eftersom om gränsvillkor uppfylla inte kravet. så länge price > level1 då kommer alltid både level1&2 rabatter att exekvera vilken är vilket ger rabbat på level 1 + 2 ********\n")
#price = input("Välkommen, köp något dyrt: ")
#price = float(price)
#if price > level1:
#   print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
#    discount = discount + 10
#if price >= level2:
#    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
#    discount = discount + 25

#final_price = price * (100 - discount)/100
#print("Efter rabatter blir priset ......." + str(final_price))


is_member = False
level1 = 100
level2 = 300
discount = 0

price = float(input("Välkommen, köp något dyrt: "))
medlem = input(" Är du medlem? 'ja' eller 'nej':")
if medlem == 'ja':
    is_member = True
else:
    is_member = False

if is_member :
    if level2 > price >= level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
        discount = discount + 10
        if price >= level2:
            print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
            discount = discount + 25
else:
    print("")
final_price = price * (100 - discount)/100
print("Efter rabatter blir priset ......." + str(final_price))