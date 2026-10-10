inventorius = {}
for vieta in range(1, 10):
    inventorius[str(vieta)] = None

while True:
    print("\nMINECRAFT INVENTORIUS")
    print("1 - Pasiimti vieną daiktą")
    print("2 - Peržiūrėti inventorių")
    print("3 - Perkelti daiktus į kitą langelį")
    print("0 - Baigti")
    veiksmas = input("Pasirinkite veiksmą: ").strip()

    if veiksmas == "0":
        break

    elif veiksmas == "1":
        daiktas = input("Daikto pavadinimas (maišeliui įveskite bundle): ").strip().lower()
        if daiktas == "":
            print("Įveskite daikto pavadinimą.")
            continue

        paimtas = False

        if daiktas != "bundle":
            for vieta in inventorius:
                langelis = inventorius[vieta]
                if langelis != None:
                    if langelis["daiktas"] == daiktas and langelis["kiekis"] < 64:
                        langelis["kiekis"] += 1
                        paimtas = True
                        break

        if paimtas == False:
            for vieta in inventorius:
                if inventorius[vieta] == None:
                    inventorius[vieta] = {
                        "daiktas": daiktas,
                        "kiekis": 1,
                        "turinys": []
                    }
                    paimtas = True
                    break

        if paimtas == False and daiktas != "bundle":
            for vieta in inventorius:
                langelis = inventorius[vieta]
                if langelis != None:
                    if langelis["daiktas"] == "bundle" and len(langelis["turinys"]) < 5:
                        langelis["turinys"].append(daiktas)
                        paimtas = True
                        break

        if paimtas == True:
            print("Daiktas paimtas:", daiktas)
        else:
            print("Daiktas nepaimtas: inventoriuje nėra vietos.")

    elif veiksmas == "2":
        for vieta in inventorius:
            langelis = inventorius[vieta]
            if langelis == None:
                print(vieta, "- Tuščia")
            elif langelis["daiktas"] == "bundle":
                print(vieta, "- bundle, užimta vietų:", len(langelis["turinys"]), "/ 5")
                print("  Maišelio turinys:", langelis["turinys"])
            else:
                print(vieta, "-", langelis["daiktas"], "kiekis:", langelis["kiekis"])

    elif veiksmas == "3":
        is_kur = input("Iš kurio langelio perkelti (1-9): ").strip()
        i_kur = input("Į kurį langelį perkelti (1-9): ").strip()

        if is_kur not in inventorius or i_kur not in inventorius:
            print("Langelių numeriai turi būti nuo 1 iki 9.")
        elif is_kur == i_kur:
            print("Pasirinkite skirtingus langelius.")
        elif inventorius[is_kur] == None:
            print("Pasirinktas langelis tuščias.")
        else:
            laikinas = inventorius[i_kur]
            inventorius[i_kur] = inventorius[is_kur]
            inventorius[is_kur] = laikinas
            print("Langeliai sukeisti vietomis.")

    else:
        print("Neteisingas pasirinkimas.")
