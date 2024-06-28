# Aufgabe 7 - Mehrere Dateien zu einem Wörterbuch zusammenfügen
def alters_der_leute():
    namen = open("names.txt", "r")
    alter = open("ages.txt", "r")
    paare = {}
    meine_namen = namen.readlines()
    meine_alter = alter.readlines()
    # Namen und Alter durchlaufen und zu Paaren zusammenfügen
    for i in range(len(meine_alter)):
        paare[meine_namen[i].strip("\n")] = int(meine_alter[i].strip("\n"))
    # Das resultierende Wörterbuch ausgeben
    print(paare)

alters_der_leute()