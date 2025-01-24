def kvittokompis():
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")

    total = 0

    while True:
        belopp = input("Skriv in ett belopp: ")

        if belopp.lower() in ["quit", "avsluta"]:
            break

        try:
            total += float(belopp)
        except ValueError:
            print("Ogiltigt belopp, försök igen.")

    print(f"Det blir {total} kr totalt. Välkommen åter!")


kvittokompis()