# Aufgabe 1 - Datei erstellen, öffnen, schreiben, lesen
def neue_datei():
    # Datei im Schreib-/Lesemodus öffnen (w+)
    meine_datei = open("aufgabe1_datei.txt", "w+")
    # Text in die Datei schreiben
    meine_datei.write("Versuche es nicht! Tu es oder tu es nicht. Es gibt kein Versuchen. - Yoda\n")
    # Zum Anfang der Datei zurückkehren
    meine_datei.seek(0)
    # Den Inhalt der Datei lesen und ausgeben
    print(meine_datei.read())
    # Datei schließen
    meine_datei.close()

neue_datei()