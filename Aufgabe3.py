# Aufgabe 3 - Bestimmte Zeichen in der Datei zählen
def buchstaben_zaehlen(buchstabe):
    # Datei im Lese-/Schreibmodus öffnen (r+)
    meine_datei = open("aufgabe1_datei.txt", "r+")
    buchstaben_zaehler = 0
    # Alle Zeichen der Datei durchlaufen
    for zeichen in meine_datei.read():
        # Zeichen in Kleinbuchstaben umwandeln und vergleichen
        if zeichen.lower() == buchstabe:
            buchstaben_zaehler += 1
    # Ergebnis ausgeben, abhängig davon, ob der gesuchte Buchstabe ein Leerzeichen ist
    if buchstabe == " ":
        print("Es gibt", buchstaben_zaehler, "Wörter in der Textdatei.")
    else:
        print("Es gibt", buchstaben_zaehler, buchstabe, "in der Textdatei.")
    # Datei schliessen
    meine_datei.close()

buchstaben_zaehlen("w")