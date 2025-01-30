#Veckouppgift4_8: pretty_print
# Funktionen skriva ut innehållet i en lista lite snyggare
def pretty_print(item_list):
    if not item_list:   # Kontrollera om listan är tom
        print("Listan är tom.")
    else:
        print("Listan har",len(item_list,),"element")  # Skriv ut antalet element i item_listan
        for index, element in enumerate(item_list, start =1):  # Skriv ut varje element i item_listan
            print(index, element)

pretty_print(["a","b","c",3.14,"Bra jobbat!"])