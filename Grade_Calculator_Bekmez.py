################################################################################
# Python challenge: Grade calculator
# Name: *Emirhan Bekmez*
# Date: *04.03.2022*
# Version: *0.1*
################################################################################

def main():
    while True:
        test_punkte = input("Gib deine Punkte an was du auf den Test bekommen hast: ")
        test_punkte = int(test_punkte)
        if test_punkte >= 0 and test_punkte <= 20:
            break
        else:
            print("Ungültiger Eingabe, Das Zahl muss zwischen 0 und 20 liegen!")
    while True:
        pruefungs_punkte = input("Gib deine Punkte an was du auf den Pruefung bekommen hast: ")
        pruefungs_punkte= int(pruefungs_punkte)
        if pruefungs_punkte >= 0 and pruefungs_punkte <= 70:
            break
        else:
            print("Ungültiger Eingabe, Das Zahl muss zwischen 0 und 70 liegen!")


    while True:
        mundl_praesi_angetreten = input("Waren sie bei der muendlichen Praesentation anwesend?")
        if mundl_praesi_angetreten == "ja":
            #angetreten = True
            mundl_praesi_punkte = int(input("Wie viele Punkte hast du auf die muendliche Praessentation bekommen?: "))
            if 0 <= mundl_praesi_punkte <= 10:
                break
        elif mundl_praesi_angetreten == "nein":
            print("Du musst die Praesentation machen um Punkte zu erhalten! ")
            #angetreten = False
        else:
            print("Ungueltiger Eingabe, Bitte Antworte mit ja oder nein! ")



    notenberechnung(p_add(test_punkte, pruefungs_punkte, mundl_praesi_punkte))


def p_add(test_punkte, pruefungs_punkte, mundl_praesi_punkte):

    gesamt_test_punkte = test_punkte + pruefungs_punkte + mundl_praesi_punkte
    return gesamt_test_punkte

def notenberechnung(gesamt_test_punkte):
    if(gesamt_test_punkte >= 0 and gesamt_test_punkte <50):
        print("Nicht Genuegend (5)")
    elif(gesamt_test_punkte >= 50 and gesamt_test_punkte <65):
        print("Genuegend (4)")
    elif(gesamt_test_punkte >= 65 and gesamt_test_punkte <80):
        print("Befriedigend (3)")
    elif(gesamt_test_punkte >= 80 and gesamt_test_punkte <90):
        print("Gut (2)")
    elif(gesamt_test_punkte >= 90 and gesamt_test_punkte <=100):
        print("Sehr gut (1)")
    else:
        print("Fehler")


if __name__ == '__main__':
    main()