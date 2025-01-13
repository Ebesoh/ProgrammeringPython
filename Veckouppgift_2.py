#*****************************************************
#2 Diskutera i grupp
#Rätta eventuella fel. Vad gör koden?
#x = 100  # biljettpris
#y = 200  # pengar på fickan
#print("Det blir " + (y - x) " kronor över.")
#z = 200 - 100 / 2
#print("Hälften är: " + z)

#Kom på bättre namn, i stället för x, y och z.
#********************************************************

#Rättning av eventuella fel i veckouppgift 2.
# Koden beräknar hur mycket pengar som återstår i fickan efter biljettköp, samt hälften av det belopp som finns kvar efter biljettköpet.

biljettPris: float = 100                           # biljettpris
PengarFickan: float = 200                          # pengar på fickan
PengarOver: float = PengarFickan - biljettPris     # Pengar över efter biljett köp
HalftenPengarOver = PengarOver/2                   # Hälften av pengar över efter biljett köp

print("  Det blir " , PengarOver,"kronor över.")   # Ett sätt att skriva ut pengar över efter biljatt köp

values = ["  Det blir ",PengarOver,"kronor över."]
print(*values)                                     # Ett alternativt sätt att skriva ut pengar över efter biljatt köp

print("Hälften är:", HalftenPengarOver)            # Hälften av pengar över efter biljett köp



