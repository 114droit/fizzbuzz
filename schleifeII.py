while True:
    zahl = input("Bitte gib eine Zahl ein")
    if (int(zahl) % 2) >= 0:
        print("Diese Zahl ist ungerade")
    elif (int(zahl) % 2) == 0:
        print(f"Deine Eingabe war {zahl} und ist gerade. Programm wird beendet")
        break
    else:
        print("Das ist keine Zahl")