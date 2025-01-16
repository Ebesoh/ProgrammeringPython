#Veckouppgift_4
#1a
#1a Det är ca 470 km mellan Stockholm och Göteborg. Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.
# Du behöver fråga användaren hur fort man ska köra, i km/h.
# Programmet frågar användaren hur snabbt hen kör och beräknar sedan hur lång tid i timmar det tar att köra från Stockholm till Göteborg
import math
import datetime

Avstand_Stock_Got = 470
ForareHastighet = float (input( "skriv in hur fort du kör: "))
RestidTim = Avstand_Stock_Got/ForareHastighet
print("Du kör med hastighet", ForareHastighet, "km/h och det skall ta", f"{RestidTim:.2f}" , "timmar att köra från Stockholm till Göteborg")
print("Du kör med hastighet", ForareHastighet, "km/h och det skall ta", (round(RestidTim,2)) , "timmar att köra från Stockholm till Göteborg")
print("Du kör med hastighet", ForareHastighet, "km/h och det skall ta", "{:.2f}".format(RestidTim) , "timmar att köra från Stockholm till Göteborg")


#1b
En_Timmar = 60
RestidMin = RestidTim * En_Timmar
RestidTim = RestidMin // 60                                           # Beräkning av antal timmar
RestidMin = RestidMin % 60                                            # Beräkning av antal minuter
print("Du kör med hastighet", ForareHastighet, "km/h och det skall ta",RestidTim , "timmar och ", RestidMin,"minuter att köra från Stockholm till Göteborg")

""" hello """
#2
###Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. Användaren behöver skriva in längden på de två kortare sidorna.##
Motsatt_sida = float (input("Skriv in motsatt sidan längd av triangle: "))
Intill_Sida  = float (input("Skriv in intill sidan längd av triangle : "))
#sqrt_Motsatt_sida = math.sqrt(Motsatt_sida)
#sqrt_Intill_sida  = math.sqrt(Intill_Sida)
Hypotenusan =  math.sqrt( (Motsatt_sida**2) + (Intill_Sida**2) )

print("Du skrev in motsatt sidan =", Motsatt_sida)
print("Du skrev in Intill sidan  =" , Intill_Sida)
print("Hypoterusen basera på inskrivna verdena är :",(round(Hypotenusan,2)))


#3a
# Ett program som talar dagens datum
idag = datetime.date.today()
print("Idag datumet är:", idag)

#3b
sju_dagar_senare = idag + datetime.timedelta(days=7)
print("Idag datumet är:", idag, "och datumet om 7 dagar senare är", sju_dagar_senare)
