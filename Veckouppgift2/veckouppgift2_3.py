# Veckouppgift2_3
# Sportresultat
# Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
# Exempel på output:
# Matchen är över, nu ska vi räkna ut resultatet!
# Hur många mål gjorde Tottenham? 2
# Hur många mål gjorde Liverpool? 1
# Tottenham vann!
# Version 2: programmet ska tala om ifall det blev oavgjort.
# Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
# Tottenham vann med 1 mål!
# Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

#*************************Programmet frågar användaren om antalet mål som respektive lag gjorde i en Champions League-match
# och avgör sedan vilket lag som vann, om det blev oavgjort, eller med hur många mål ett lag vann med ***************************

Tottenham_goals = 0
Liverpool_goals = 0

print("The match is over, now lets calculate the score! ")
while True:
    try:
        Tottenham_goals = int ( input("How many goals did Tottenham score?: "))
        Liverpool_goals = int ( input("How many goals did Liverpool score?: "))
        break
    except ValueError:
        print("You can only input whole numbers, non whole numbers are not acceptable!")

diff = abs(Tottenham_goals - Liverpool_goals)

if Tottenham_goals > Liverpool_goals :
    if diff > 1 :
     print("Totettenham won!", " They won with ", str(diff), "goals difference!")
    else:
     print("Totettenham won!", " They won with ", str(diff), "goal difference!")
elif Liverpool_goals > Tottenham_goals:
    if diff > 1:
        print("Liverpool won!", " They won with ", str(diff), "goals difference!")
    else:
        print("Liverpool won!", " They won with ", str(diff), "goal difference!")
elif Tottenham_goals == Liverpool_goals:
    print("No team won, the match ended in a draw!", "Tottenham:", str(Tottenham_goals), "& Liverpool:", str(Liverpool_goals))