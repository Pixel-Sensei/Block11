# Aufgabe 9 - Kurze Wörter in der Datei finden
def gedicht_woerter():
    mein_gedicht = open("poem.txt", "r")
    mein_text = mein_gedicht.read()
    woerter = mein_text.split()
    # Wörter durchlaufen und kurze Wörter ausgeben
    for wort in woerter:
        if len(wort) < 4:
            print(wort, end=", ")

gedicht_woerter()