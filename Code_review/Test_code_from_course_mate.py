import math

r = math.comb(4,5)
print(r)

x= -2.5
s= math.fabs(x)
print(s)

x =math.remainder(3,2)
print(x)

i = 0
while i <= 5:
    print(i)
    i=i+1
running = True
while True:
    print("Utskriften upprepas om och om igen")
    val = input("Vill du köra programmet igen? Om ja, skriv ja om nej skriv nej: ")
    if val=="nej":
        break

for i in range(100):
    if i == 2:
        continue
    print(i)

for item in ['a','b','c']:
    print(item)