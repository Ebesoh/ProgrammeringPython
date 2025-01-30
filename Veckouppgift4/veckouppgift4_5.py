#Veckouppgift4_5: cut_edges
#Funktionen tar bort första och sista element is listan och returnerar a ny lista
def cut_edges (values):
    if not values:                #'if not values' kontrollerar om listan är tom. Om den är tom returneras ingenting
        return None
    return values[0],values[-1]   #values[0] hämtar det första elementet i listan och values[-1] hämtar det sista elementet i listan
print(cut_edges([1,2,3,4]))