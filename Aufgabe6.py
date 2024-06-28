# Aufgabe 6 - Zeichnen in Datei
def zeichnen():
    zeichne_datei = open("zeichnenDatei.txt", "w+")
    for i in range(10):
        j = 0
        while j < 10:
            for k in range(j):
                zeichne_datei.write("-")
            zeichne_datei.write("  ")
            for k in range(10-j):
                zeichne_datei.write("-")
            zeichne_datei.write("\n")
            j += 1
        while j > 0:
            for k in range(j):
                zeichne_datei.write("-")
            zeichne_datei.write("  ")
            for k in range(10-j):
                zeichne_datei.write("-")
            zeichne_datei.write("\n")
            j -= 1
    # Zum Anfang der Datei zurückkehren
    zeichne_datei.seek(0)
    # Den Inhalt der Datei lesen und ausgeben
    print(zeichne_datei.read())

zeichnen()