#Veckouppgift4_: Spelet_21_v1 ( formeln: s= n(n+1)/2)
#Funktionen skriver ut första tal i talserie som är större än 21
def forsta_tal_store_an_21 ():
    total_sum = 0
    number = 1
    while True:                              #Loopen fortsätter tills summan överstiger 21.Varje iteration lägger till det aktuella talet (number) till total_sum
        total_sum = total_sum + number
        if total_sum > 21:                   #Om total_sum blir större än 21, returneras det aktuella talet (number)
            return number
        number = number +1                   #number ökas med 1 efter varje iteration.

# Anropa funktionen och skriv ut resultatet
forsta_store_tal = forsta_tal_store_an_21()
print(forsta_store_tal)
