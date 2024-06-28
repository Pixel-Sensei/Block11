# Aufgabe 2 - Neue Zeile hinzufügen, Zeilen lesen
def neue_zeile():
    # Datei im Anhänge-/Lesemodus mit UTF-8-Kodierung öffnen (a+)
    meine_datei = open("aufgabe1_datei.txt", "a+", encoding="utf-8")
    # Neuen Text in die Datei schreiben
    meine_datei.write("Wer ist der größere Narr: der Narr oder der Narr, der ihm folgt? - Obi-Wan Kenobi")
    # Zum Anfang der Datei zurückkehren
    meine_datei.seek(0)
    # Alle Zeilen der Datei lesen und ausgeben
    for zeile in meine_datei.readlines():
        print(zeile)
    # Datei schliessen
    meine_datei.close()

neue_zeile()