# Aufgabe 8 - Mehrere Dateien in neue Datei zusammenfügen
def alters_der_leute_2():
    namen = open("names.txt", "r")
    alter = open("ages.txt", "r")
    paare = open("paare.txt", "w+")
    meine_namen = namen.readlines()
    meine_alter = alter.readlines()
    # Namen und Alter durchlaufen und in die neue Datei schreiben
    for i in range(len(meine_alter)):
        paare.write(meine_namen[i].strip("\n"))
        paare.write(": ")
        paare.write(meine_alter[i].strip("\n"))
        paare.write("\n")
    # Zum Anfang der Datei zurückkehren
    paare.seek(0)
    # Den Inhalt der neuen Datei lesen und ausgeben
    print(paare.read())

alters_der_leute_2()