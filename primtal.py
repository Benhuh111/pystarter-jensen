# Planering av programmeringsuppgiften:
# För att lösa problemet planerade jag att först skriva en funktion 'är_primtal()' för att kontrollera om ett givet tal är ett primtal.
# Sedan skapade jag en funktion 'hitta_primtal()' som använder 'är_primtal()' för att hitta alla primtal upp till en given gräns.
# Slutligen skapade jag en huvudfunktion 'main()' för att läsa in ett tal från användaren och skriva ut alla primtal upp till det givna talet.

# Felsökning av enkla syntaxfel:
# Jag använder try-except för att hantera felaktig inmatning och andra fel som kan uppstå under körningen av programmet.
# Jag kontrollerar också om det givna talet är mindre än 2 för att undvika att försöka hitta primtal i intervallet om det inte finns några.

# Utvärdering av programmet:
# Programmet fungerar som förväntat och listar alla primtal upp till det givna talet.
# Det är användarvänligt och kan hantera felaktig inmatning från användaren.
# Jag anser att det är effektivt och ger korrekta resultat för att hitta primtal i ett visst intervall.


def är_primtal(num):
    """Funktion för att kontrollera om ett tal är ett primtal."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def hitta_primtal(max_gräns):
    """Funktion för att hitta alla primtal upp till en given gräns."""
    primtal_lista = []
    for num in range(2, max_gräns + 1):
        if är_primtal(num):
            primtal_lista.append(num)
    return primtal_lista

def main():
    """Huvudfunktionen för att köra programmet."""
    try:
        max_tal = int(input("Ange ett heltal: "))
        if max_tal < 2:
            print("Inga primtal finns i intervallet.")
        else:
            primtal = hitta_primtal(max_tal)
            print(f"Primtal mellan 1 och {max_tal}:")
            for primtal_num in primtal:
                print(primtal_num, end=" ")
    except ValueError:
        print("Felaktig inmatning. Ange ett heltal.")

if __name__ == "__main__":
    main()
