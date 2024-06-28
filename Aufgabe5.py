# Aufgabe 5 - Zeilen aus Einkaufsliste entfernen
def items_entfernen(item):
    einkaufs_datei = open("meineEinkaufsDatei.txt", "r+")
    zeilen = einkaufs_datei.readlines()
    # Position der Datei auf Anfang setzen
    einkaufs_datei.seek(0)
    # Zeilen durchlaufen und nur die Zeilen schreiben, die nicht das zu entfernende Element enthalten
    for zeile in zeilen:
        if zeile.strip("\n") != item:
            einkaufs_datei.write(zeile)
        einkaufs_datei.truncate()
    # Zum Anfang der Datei zurückkehren
    einkaufs_datei.seek(0)
    # Den aktualisierten Inhalt der Datei lesen und ausgeben
    print(einkaufs_datei.read())

items_entfernen("Käse")