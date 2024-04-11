# Dokumentation:
# Detta program beräknar hur mycket pengar man får på ett bankkonto
# om man sätter in en viss summa och låter den stå inne under ett
# visst antal år med en given räntesats. Programmet frågar användaren
# efter räntesatsen och visar sedan en tabell som visar hur kapitalet
# växer år för år.

# Planeringen av programmeringsuppgiften:
# Först behöver vi få input från användaren om räntesatsen.
# Sedan använder vi en enkel formel för att beräkna kapitalet efter varje år:
# Nytt kapital = gammalt kapital * (1 + räntesats/100)
# Vi upprepar detta för varje år och visar resultatet i en tabell.

# Felsökning av enkla syntaxfel:
# - Se till att alla variabler är korrekt namngivna och definierade.
# - Kontrollera att alla parenteser är korrekt avslutade.
# - Använd avskiljare och mellanslag för tydlighetens skull.

# Skriv en kort utvärdering av programmet:
# Programmet fungerar som förväntat och ger användaren en tydlig
# översikt över hur kapitalet växer över tid med den angivna räntesatsen.
# En förbättring kan vara att lägga till felhantering för ogiltig input,
# såsom bokstäver istället för siffror, för att göra programmet robustare.

# Python-programmet:

def main():
    # Fråga användaren efter räntesatsen
    räntesats = float(input("Ange räntesatsen (t.ex. 3.5 för 3.5%): "))
    
    # Ange det ursprungliga kapitalet
    kapital = 100000  # 100 000 kronor
    
    print("År\tKapital")
    print("------------------")
    
    # Beräkna kapitalet för varje år och skriv ut det i en tabell
    for år in range(1, 12):
        kapital *= (1 + räntesats / 100)
        print(f"{år}\t{round(kapital, 2)} kr")

if __name__ == "__main__":
    main()
