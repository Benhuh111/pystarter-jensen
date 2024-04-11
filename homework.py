# Dokumentation för Prisberäkningsprogrammet

# Planering av programmeringsuppgiften:
# Målet med detta program är att beräkna priset inklusive moms baserat på det pris exklusive moms som användaren anger. 
# Programmet tar in priset exklusive moms som inmatning från användaren, multiplicerar det med 1.25 (25% moms) och 
# visar det resulterande priset inklusive moms som utdata.

# Felsökning av enkla syntaxfel:
# - Se till att användaren anger en numerisk inmatning för priset exklusive moms.
# - Använd exceptionhantering för att hantera felaktig inmatning.

# Kort utvärdering av programmet:
# Programmet är enkelt och uppfyller sitt syfte att beräkna priset inklusive moms. 
# Det hanterar felaktig inmatning genom att använda float() för att konvertera inmatningen till ett flyttal och 
# genom att använda exceptionhantering för att hantera icke-numeriska inmatningar. 
# För att förbättra programmet kan man överväga att lägga till ytterligare felhantering och validering av inmatningen.
 
# Användaren anger pris exkl. moms som indata
pris_exkl_moms = input("Ange pris exkl. moms: ")

try:
    # Konvertera inmatningen till ett flyttal
    pris_exkl_moms = float(pris_exkl_moms)

    # Beräkna priset inklusive 25% moms
    pris_inkl_moms = pris_exkl_moms * 1.25

    # Visa priset inklusive moms som utdata
    print(f"Pris inkl. moms: {pris_inkl_moms:.2f}")

except ValueError:
    # Felhantering för icke-numerisk inmatning
    print("Felaktig inmatning. Ange ett numeriskt värde för priset exkl. moms.")
