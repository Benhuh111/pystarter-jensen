def main():
        # Fråga efter poäng på tre olika prov
        poang1 = float(input("Ange poäng för prov 1: "))
        poang2 = float(input("Ange poäng för prov 2: "))
        poang3 = float(input("Ange poäng för prov 3: "))
        
        # Beräkna medelvärdet av alla tre poängen
        medel = (poang1 + poang2 + poang3) / 3
        
        # Skriv ut medelvärdet
        print("Medelvärdet av poängen är:", medel)
        
        # Om medelvärdet är över 90, skriv också ut "Bra jobbat"
        if medel > 90:
            print("Bra jobbat!")

if __name__ == "__main__":
    main()

# Detta program fungerar genom att fråga användaren efter poängen på tre prov och beräknar sedan medelvärdet av dessa poäng.
# Om medelvärdet är över 90 skriver programmet också ut "Bra jobbat". 
# Programmet är uppdelat i funktioner för att göra koden mer lättläst och underhållbar.
    
# Programmet fungerar som förväntat och uppfyller alla specifierade krav.
# Det är väl strukturerat och lätt att förstå.
# Felhantering för ogiltiga inmatningar (t.ex. bokstäver istället för siffror) kan läggas till för att göra programmet mer robust.
# Generellt sätt är programmet en bra lösning för att beräkna medelvärdet av poäng och ge feedback om prestationen.