# Veckouppgift2_2
#2 Balder
#För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!

#Fråga användaren hur lång man är (i cm)
#Skriv ut antingen "Du får åka!" eller "Du får inte åka"

#Skriv in följande värden för att testa att ditt program gjort rätt:
#121 cm (får inte åka)
#130 cm (får åka)
#155 cm (får åka)

#Diskutera:
#Varför just tre värden?
###Svar: För det är viktigt att testa gränsvärdena
#Varför dessa värden?
###Svar: Dessa värden testa hur programmet reagerar när användaren är längre, kortare och lika med längd krav för att åka Balder på Lisebery
#Skulle det vara bra att lägga till testvärdet 129 cm? Ja, det skulle vara bra att testa 129cm  och 131cm. Med detta testa man gränsvärden

#********************************** Programmet kontrollerar användarens längd för att bekräfta om de uppfyller längdkravet för att åka Balder på Liseberg *************
height_requirement = 130
user_height = float ( input("Please input your height in cm: "))

if user_height < 130:
    print( " Sorry you can't ride Balder, one must be",str(height_requirement), "cm tall to ride Balder")
elif user_height >= 130:
    print(" Congratulation!! with a height of ", str(user_height), " cm, you can ride Balder")