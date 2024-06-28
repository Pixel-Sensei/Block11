# Aufgabe 4 - Liste in neue Datei schreiben
def liste_datei():
    einkaufsliste = ["Brot\n", "Milch\n", "Käse\n", "Apfel\n"]
    einkaufs_datei = open("meineEinkaufsDatei.txt", "w+")
    # Liste in die Datei schreiben
    einkaufs_datei.writelines(einkaufsliste)
    # Zum Anfang der Datei zurückkehren
    einkaufs_datei.seek(0)
    # Den Inhalt der Datei lesen und ausgeben
    print(einkaufs_datei.read())

liste_datei()