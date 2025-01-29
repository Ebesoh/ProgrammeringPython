#veckouppgift_4_1_1a
from Veckouppgift3.veckouppgift3_1 import index, counter


def foo(t):
    print("test")
foo("")
foo("hej")

#veckouppgift_4_1_1b
def fun1(x,y):
    return x*y
print(3,5)               # Det bara skriva ut 3, 5 och fun1 är oanvänd


#veckouppgift_4_1_1c
def fun1(x,y):
    return x*y
print(fun1(3,5))   # X*Y= 15 skrivs ut för att fun1 har blivit anropat

#veckouppgift_4_1_1d
def fun2(i):
    return 5 * i
x= 2
y= 3
a = fun2(fun2(x) + fun2(y))
print(a)                      # Det som skrivs ut skall vara 125: fun2(x) = 10, fun2(y) = 15 och fun2(10+15) = 125

#veckouppgift_4_1_1e
a= 5
def fun3(a):
    a +=1
    return a                  # funktionen returnerar 'a'
a+=2
print(a)                      # 'a' som skrivs ut = 5 + 2 = 7 eftersom funktionen är inte anropat
print(fun3(a))                # Funktionen används men själva fun3 returnerar ingenting. Genom att lägga return 'a' i fun3 skall utskriften vara '8'

#veckouppgift_4_1_1f
def foo(i):
    return 2*i*i

def goo(x,y):
    return x*y
#a =goo(foo,3)                   # Funktionen är inte anropat på rätt sätt. print(a) skall inte skriva ut någonting.
a1 =goo(foo(2),3)             # lösningen: Genom att anropa funktionen foo() med ett 'i' värde lösa man problemet
#print(a)                        # Skrivs ut ingenting
print(a1)                        # Skrivs ut: f00(2) = 2*2*2 = 16 * 3 = 24

#veckouppgift_4_1_1g
def is_number(x):
    if isinstance(x,int):
        return True
    elif isinstance(x,float):
        return False
    return False

print(is_number(5.5))            # returnerar 'False'
print(is_number(42))             # returnerar 'True'
print(is_number(""))             # returnerar 'False'

#veckouppgift_4_1_1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding", "eating"]))

#veckouppgift_4_1_1i
#Lista ut vad som är funktionens syfte, baserad på namn och sammanhang:
##Svar: Funktionen returnerar lägsta värde i listan
#Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
##Svar: -11, 0, 0
#Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    #counter = 0                  #Variabeln counter ska inte initialiseras till '0' eftersom '0' kanske inte är det minsta värdet i listan. Istället bör den initialiseras till det första elementet i listan för att säkerställa att rätt lägsta värde hittas.
    if len(numbers) == 0:         #Här kontrolleras om listan är tom
        print("The list is empty.")
        return
    counter = numbers[0]          # Initialisering av variabeln counter med första elementet i listan
    for item in numbers:
        if item < counter:
            counter = item
    print(f"the smallest item is:{counter}")

find_min([10,3-4,-11,])
find_min([])
find_min([100])