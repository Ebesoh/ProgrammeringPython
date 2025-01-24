#veckouppgift3_2

from Code_review.Test_code_from_course_mate import number

print("\n********************Veckouppgift3_2_1a***********************")
answer = 0
for i in range(1,11):
    answer += i
print("Summan av talen 1 till 10 är:" + str(answer))

#veckauppgift3_2_1b
print("\n********************Veckouppgift3_2_1b***********************")
print("Räknar summan 1-100 med 'for-loop'")
summa = 0
for i in range(1,101):
    summa += i
print("Summan av talen 1 till 100 är:" + str(summa))

#veckauppgift3_2_1c
print("\n********************Veckouppgift3_2_1c***********************")
print("Räknar summan 1-100 med 'while-loop'")
summa = 0
increment =0
while increment <= 100:
    summa = summa + increment
    increment +=1
print("Summan av talen 1 till 100 är:" + str(summa))

#veckauppgift3_2_2
lista = [2,4,3,7,5,1,6,2]
total = sum(lista)
#print(lista.sort())
#print(lista.reverse())
print("Total sum of numbers from list",total)

total = 0
for num in lista:
    total += num # total = total + num
print("Total sum of numbers from list",total)

#veckauppgift3_2_3
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
print(lista[6])
print(lista[7])
print("Index 2", lista.index(2))
print(len(lista))
#lista.count(2)
print("2 appears in lista ",lista.count(2), "times")
print(lista)
lista.reverse()
print(lista)
lista.append(2)
print("Lista appended with 2", lista)
lista.remove(2)
print("2 removed from lista", lista)
lista.reverse()
print(lista)
print(lista.__len__())
lista.insert(9, 10)
print(lista)
lista.insert(0,0)
print(lista)
lista.insert(1,1)
print(lista)
lista.remove(2)
print(lista)
lista.pop(3)
print(lista)

#veckauppgift3_2_3a
movies_name = ["God father 1", "The devils advocate","The Irishman","GoodFellas" ]
print(movies_name)

#veckauppgift3_2_3b
movies_name.append("Fellowship of the ring")
print(movies_name)

#veckauppgift3_2_3c
movies_name.insert(0,"The two towers")
print(movies_name)

#veckauppgift3_2_3d
print("Index 'Fellowship of the ring' is:",movies_name.index("Fellowship of the ring"))

#veckauppgift3_2_3e
movies_name.remove("GoodFellas")
print("Index 'Fellowship of the ring' is:",movies_name.index("Fellowship of the ring")) # Yes the index position changed from 5 to 4

#veckauppgift3_2_3f
print(movies_name.__len__())

#veckauppgift3_2_3g
movies_name.reverse()
print(movies_name)

#veckauppgift3_2_3h
movies_name.sort()
print(movies_name)