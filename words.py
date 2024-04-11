# Planering av programmeringsuppgiten:
# Först definierar vi en 'main()'-funktion som är huvudfunktionen i programmet.
# Vi ber användaren att ange en mening.
# Vi delar upp meningen i ord och beräknat antalet ord.
# Vi skriver ut antalet ord och det första och sista ordet.

# Felsökning av enkla syntaxfel:
# Vi använder grundläggande stränghantering och listoperationer, så risken för syntaxfel är låg.
# Men om det finns några fel, kommer Python att generera lämpliga felmeddelanden som hjälper oss att identifiera och korrigera dem.

# Utvärdering av programmet:
# Programmet fungerar som förväntat och uppfyller alla krav i uppgiften. 
# Det ber användaren att ange en mening, räknar antalet ord och skriver ut det första och sista ordet. 
# Det är enkelt att använda och ger önskat resultat.


def main():
    # Läs in en mening från användaren
    mening = input("Skriv in en mening bestående av minst två ord: ")

    # Dela upp meningen i ord
    ord_lista = mening.split()

    # Beräkna antalet ord
    antal_ord = len(ord_lista)

    # Skriv ut antalet ord
    print(f"Du skrev {antal_ord} ord.")

    # Skriv ut det första ordet om det finns minst ett ord
    if antal_ord >= 1:
        print(f"Det första ordet är \"{ord_lista[0]}\".")

    # Skriv ut det sista ordet om det finns minst ett ord
    if antal_ord >= 2:
        print(f"Det sista ordet är \"{ord_lista[-1]}\".")

if __name__ == "__main__":
    main()
