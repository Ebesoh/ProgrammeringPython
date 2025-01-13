#****************************************************************************************************************************************************************************************
#Veckouppgift_3
#Använda variabler och datatyper
#1a Använd input för att be användaren om ett heltal. Spara värdet i en variabel. Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
#Kodexempel med input:
#x = input("Fråga här")
#from main import summa

#1b Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
#Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.


#2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
#Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.

#2b Gör om programmet så att användaren kan skriva in en procentsats.
#Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 k
#*****************************************************************************************************************************************************************************************

# 1a
tal1 = int(input("Skriv in ett heltal: "))                   # Ber användaren att skriva in heltal
print("Talet som skriv in är : ", tal1)                      # Skriv ut heltal för att verifiera att programmet har skrivit rätt

#1b
tal2 = int(input("Skriv in ett annat heltal: "))             # Ber användaren att skriva in ett annat heltal
summa = tal1 + tal2                                          # Summering av 2 tal ( tal 1 + tal 2)
print("Summan av tal 1 och tal 2 är: ", int(summa))          # Utskrivning av 2 tal summa

#2a
JackaPris = 2000
rea_procent = 50
slut_pris = JackaPris - (JackaPris * rea_procent/100)                      # slut pris beräkning inklusive 50 % rabbat
print("Att betala för vinterjacka inklusive rabbat:", float(slut_pris))    # Utskriving av slut pris

#2b
rea_procent = float(input("Skriv in procentsats: "))                        # Begära användare att skriva in procentsats
slut_pris = JackaPris - (JackaPris * rea_procent/100)                       # Beräkning av slut pris med inskrivna användarens procentsats
print("Att betala för vinterjacka inklusive rabbat:", float(slut_pris))     # Utskrivning av slut pris inklusive användares procentsats
