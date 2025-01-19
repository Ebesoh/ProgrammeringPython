is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Väkommen, köp något dyrt: ")
price = float(price)
if level2> price > level1:
    print("Nivå 1 och 10% rabatt.")
    discount = discount + 10
elif price >= level2:
    print("Nivå 2 och 25% rabatt.")
    discount = discount + 25
final_price = price * (100 - discount)  / 100
print("Efter rabatter blir pricet... " + str(final_price))