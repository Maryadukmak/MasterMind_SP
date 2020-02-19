import code_raden as fl

def player_secretcode_pc():  # voor computer guess
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    secret_code = []
    while len(secret_code) < 4:
        code_input = (input("Geef me de kleuren:")).lower()
        if code_input not in kleuren:
            print("voer een geldig kleur in!")
        elif code_input == "stop":
            print("Het spel is gestopt.")
            return secret_code
        else:
            secret_code.append(code_input)
    print("De gekozen secret code is: {} ".format(secret_code))
    return secret_code


def computer_guess_m():
    secret_code = player_secretcode_pc()
    print("Maak de secret code,\n" 
          "Kies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. \r")
    return secret_code


def alle_mogelijk_gok():
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    alle_mogelijkheden = []
    for i in kleuren:
        for k in kleuren:
            for c in kleuren:
                for g in kleuren:
                    alle_mogelijkheden.append([i, k, c, g])
                    alle_mogelijkheden.sort()
    return alle_mogelijkheden


def verwijder_gokken(secret_code, alle_mogelijkheden):   # Bron for the while loop : Iwan
    eerstekeer = 0
    while True:
        if eerstekeer == 0:
            gok1 = ['wit', 'wit', 'rood', 'groen']
            eerstekeer = 1
        else:
            gok1 = alle_mogelijkheden[0]
        lijst_return = []
        print(gok1)
        if secret_code == gok1:
            print("De computer heeft je secret code binnen {} keer geraden !".format(eerstekeer))
            break
        feedback1 = fl.vergelijking(gok1, secret_code)
        for item in alle_mogelijkheden:
            a = fl.vergelijking(gok1, item)
            if a == feedback1:
                lijst_return.append(item)
        alle_mogelijkheden = lijst_return
        eerstekeer += 1


def algoritme_makkelijk(secret_code, alle_mogelijkheden):
    teller = 0
    while True:
        gok = alle_mogelijkheden[0]
        if gok == secret_code:
            print(gok)
            print("De algoritme heeft je secret code binnen {} keer geraden!".format(teller))
            break
        else:
            alle_mogelijkheden.remove(gok)
            teller += 1


def eigen_algoritme():
    secret_code = computer_guess_m()
    alle_mogelijkheden = alle_mogelijk_gok()
    teller = 0
    mogelijkheden_2 = []

    while True:
        gok1 = ['wit', 'wit', 'rood', 'groen']
        gok2 = ["wit", 'rood', 'groen', 'geel']
        if secret_code == gok1:
            print(gok1)
            print("De computer heeft je secret code binnen 1 stap geraden!")
            break
        elif secret_code == gok2:
            print(gok2)
            print("De computer heeft je secret code binnen 2 stappen geraden !")
            break
        else:
            a = fl.vergelijking(gok1, secret_code)
            b = fl.vergelijking(gok2, secret_code)
            if str(a) == str(b) or str(a) > str(b):
                for item in alle_mogelijkheden:
                    c = fl.vergelijking(gok1, item)
                    if a == c:
                        mogelijkheden_2.append(item)
            elif str(b) < str(a):
                for item in alle_mogelijkheden:
                    d = fl.vergelijking(gok2, item)
                    if b == d:
                        mogelijkheden_2.append(item)
            else:
                gok3 = mogelijkheden_2[0]
                print(gok3)
        alle_mogelijkheden = mogelijkheden_2
        teller += 1
        print(len(mogelijkheden_2))
