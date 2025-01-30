#Veckouppgift4_7
# Funktionen returnerar medelvärdet av två tal (både skall vara tal).
def average (x,y):
    if not isinstance(x,(int,float)):                # Kontrollerar att 'x' är ett tal
        print("Input 'x' must be an int or float")
        return False
    if not isinstance(y, (int, float)):              # Kontrollerar att 'y' är ett tal
        print("Input 'y' must be an int or float")
        return False
    else:
        result = (x + y) / 2
        return result

print(average(2,10))