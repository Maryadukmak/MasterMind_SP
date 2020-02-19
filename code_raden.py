import random


def keuze_m():
    print("---Mastermind game---")
    while True:
        keuze = (input("Kies een van de opties:\n""1.Raad de code\n""2.Maak de code\n"
                       "3.Maak de code met makkelijk algoritmen\n""'\r"))
        if '1' in keuze:
            start()
            break
        elif '2' in keuze:
            print('\r')
            verwijder_gokken(computer_guess_m(), alle_mogelijk_gok())
            break
        elif '3' in keuze:
            algoritme_makkelijk(computer_guess_m(), alle_mogelijk_gok())
            break
        else:
            print("Voer een geldige keuze in !\r")


def input_vragen():  # voor player guess
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    gok = []
    while len(gok) < 4:
        code_input = (input("Guess de kleuren:")).lower()
        if code_input == "stop":
            print("Het spel is gestopt.")
            exit()
        if code_input not in kleuren:
            print("Voer een geldig kleur in!")
        else:
            gok.append(code_input)
    return gok


def start():
    print(" \nJe gaat de code raden, dus...\nKies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. ")
    gok = input_vragen()
    secret_code = random_secret_code()
    klopt_positie, klopt_kleuren = vergelijking(gok, secret_code)
    feedback(klopt_positie, klopt_kleuren)


def random_secret_code():
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    #secret_code_random = ["wit",'rood', 'groen', 'groen']
    secret_code_random = random.sample(kleuren, 4)
    return secret_code_random


def vergelijking(gok, secret_code):  # Bron: Adam (de twee lijsten methode)
    if gok == secret_code:
        return 4, 0
    else:
        while gok != secret_code:
            klopt_kleuren = 0  # wit
            klopt_positie = 0  # zwart
            code_speler_list = []
            code_list = []
            for kleur_index in range(0, 4):  # zwart
                if gok[kleur_index] == secret_code[kleur_index]:
                    klopt_positie += 1
                else:
                    code_speler_list.append(gok[kleur_index])
                    code_list.append(secret_code[kleur_index])
            for items in code_speler_list:  # wit
                for items2 in code_list:
                    if items == items2:
                        klopt_kleuren += 1
                        code_list.remove(items2)
                        break
                else:
                    continue
            return klopt_positie, klopt_kleuren


def feedback(klopt_positie, klopt_kleuren):
    count_aantal_pogingen = 1
    while klopt_positie != 10:
        if count_aantal_pogingen == 10:
            print("Je hebt de maximale aantal pogingen bereikt. Probeert het opnieuw")
            exit()
        elif klopt_positie == 4:
            print("Goed gedaan! Je bent een Mastermind!")
            print("Je hebt het binnen {} pogingen in gedaan.".format(count_aantal_pogingen))
        else:
            print("\rHet aantal zwart pin(s) is {} \nHet aantal wit pin(s) is {}\r".format(klopt_positie, klopt_kleuren))
            input_vragen()
        count_aantal_pogingen += 1
        print(count_aantal_pogingen)

keuze_m()
