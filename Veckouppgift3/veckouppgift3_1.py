#veckauppgift3_1_1
# Vad som skrivs ut är: 5, 7,9,11,13,15
print("\n********************Veckouppgift3_1_1***********************")
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2

#veckauppgift3_1_2
#Vad som skrivs ut är: 0, 1, 2,3,4, ,6,7,8,9
print("\n********************Veckouppgift3_1_2***********************")
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
        i = i +1

#veckauppgift3_1_3
# Vad blir summan? Skriv ner din bästa gissning innan du kör koden. Gissning; 0,1,3,6,10,15
print("\n********************Veckouppgift3_1_3***********************")
counter = 0
for i in range(6):
    #counter += i
    counter = counter +  i
    print(counter)

#veckauppgift3_1_4
# För att förstå koden kan du sätta ut brytpunkter och köra med debugging. Det kan också underlätta att skriva samtidigt med papper och penna.
# Kode skriva ut x = x-y när y är jämna tal och x = x +(y*y) när y är udda tal: 1,-1,8,4,29,23,72,64,145
print("\n********************Veckouppgift3_1_4***********************")
x = 0
y = 1
print("y|", "X_for_Y_even|", "X_for_Y_odd")
while y < 10:
    print(y,x)
    if y % 2 == 0:
        x-= y
        #breakpoint()
        print("X for Y_even is: ", x)
    else:
        x+=y*y
        print("X for Y_odd is: ", x)
        #breakpoint()
    y += 1

#veckauppgift3_1_5
# Vad skrivs ut?
print("\n********************Veckouppgift3_1_5***********************")
message = "its_time_too_get_coding"
print(message[3:7])  # skrivs ut '-tim'
print(message[4:8])  # skrivs ut 'time'

#veckauppgift3_1_6
# Kan du flytta linjen ett steg åt höger?
print("\n********************Veckouppgift3_1_6***********************")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#" + s # s = s + "#"
        else:
            s += "." #  s = s+ s + "."
    print(s)
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#" + s # s = s + "#"
        else:
            s += "." #  s = s+ s + "."
    print(" " + s)
