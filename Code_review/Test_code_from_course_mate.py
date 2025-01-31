import random

def sum_over_21():
    total = 0
    while total <= 21:
        card = random.randint(1, 13)
        total += card
        print(f"Du drog: {card}, totalen är nu: {total}")
    print(f"Summan blev {total}, vilket är större än 21.")

# Exempelanvändning
sum_over_21()

def play_21():
    user_total = 0
    computer_total = 0

    # Spelaren tar kort
    while True:
        choice = input("Vill du ta ett nytt kort (ja/nej)? ").lower()
        if choice == "ja":
            card = random.randint(1, 13)
            user_total += card
            print(f"Du drog: {card}, din total är nu: {user_total}")
            if user_total > 21:
                print("Du gick över 21! Du förlorade.")
                return
        else:
            print(f"Du stannar med totalen: {user_total}")
            break

    # Datorn tar kort
    while computer_total < 17:  # Datorn stannar när den når 17 eller högre, datorn simulerade motståndare
    #while True:
        card = random.randint(1, 13)
        computer_total += card
        print(f"Datorn drog: {card}, datorns total är nu: {computer_total}")
        if computer_total > 21:
            print("Datorn gick över 21! Du vann.")
            return

    # Jämför totalsummorna
    if user_total > computer_total:
        print(f"Du vann! Din total: {user_total}, datorns total: {computer_total}")
    elif user_total < computer_total:
        print(f"Datorn vann! Datorns total: {computer_total}, din total: {user_total}")
    else:
        print(f"Det blev oavgjort! Både du och datorn har {user_total}.")

# Exempelanvändning
play_21()