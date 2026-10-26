print("GRADEMASTER")
print("Bienvenue sur GradeMaster — Votre calculateur de moyennes personnel !")
print("Calculez vos notes facilement et avec précision.")
print("Choisissez votre niveau scolaire pour commencer.\n")

cycle = input(
    "Choisissez votre cycle scolaire :\n"
    "1 - École primaire\n"
    "2 - Collège\n"
    "3 - Lycée\n"
    "Votre choix : "
).strip().lower()


def primaryschool123():
    moyenne = (
        arabe + amazighe + francais + mathematiques +
        activites_scientifiques + education_islamique +
        education_artistique + education_physique
    ) / 8
    return moyenne


def primaryschool456():
    moyenne = (
        arabe + amazighe + francais + mathematiques +
        activites_scientifiques + etudes_sociales +
        education_islamique + education_artistique +
        education_physique
    ) / 9
    return moyenne


def middleschool1():
    moyenne = (
        arabe * 3 +
        francais * 3 +
        anglais * 2 +
        mathematiques * 4 +
        education_islamique * 2 +
        etudes_sociales * 2 +
        sciences_vie_terre * 2 +
        physique_chimie * 2 +
        education_physique * 1
    ) / 21
    return moyenne


def middleschool2():
    moyenne = (
        arabe * 3 +
        francais * 3 +
        anglais * 2 +
        mathematiques * 4 +
        education_islamique * 2 +
        etudes_sociales * 2 +
        sciences_vie_terre * 2 +
        physique_chimie * 2 +
        education_physique * 1 +
        education_familiale * 1 +
        informatique * 1
    ) / 23
    return moyenne


def middleschool3():
    moyenne = (
        arabe * 3 +
        francais * 3 +
        anglais * 2 +
        mathematiques * 4 +
        education_islamique * 2 +
        etudes_sociales * 2 +
        sciences_vie_terre * 2 +
        physique_chimie * 2 +
        education_physique * 1
    ) / 21
    return moyenne

def tronc_commun():
    moyenne = (
        arabe * 2 +
        francais * 2 +
        anglais * 2 +
        mathematiques * 4 +
        physique_chimie * 4 +
        sciences_vie_terre * 3 +
        education_islamique * 2 +
        etudes_sociales * 2 +
        philosophie * 2 +
        informatique * 1 +
        education_physique * 1
    ) / 25
    return moyenne


def bac1science():
    moyenne = (
        arabe * 2 +
        francais * 2 +
        anglais * 2 +
        mathematiques * 4 +
        physique_chimie * 4 +
        sciences_vie_terre * 3 +
        education_islamique * 2 +
        etudes_sociales * 2 +
        philosophie * 2 +
        informatique * 1 +
        education_physique * 1
    ) / 25
    return moyenne


def bac1literature():
    moyenne = (
        arabe * 4 +
        francais * 3 +
        anglais * 3 +
        mathematiques * 1 +
        education_islamique * 2 +
        etudes_sociales * 3 +
        philosophie * 3 +
        informatique * 1 +
        education_physique * 1
    ) / 21
    return moyenne


def bac2science():
    moyenne = (
        arabe * 2 +
        francais * 2 +
        anglais * 2 +
        mathematiques * 4 +
        physique_chimie * 4 +
        sciences_vie_terre * 3 +
        philosophie * 2 +
        education_islamique * 2 +
        education_physique * 1
    ) / 22
    return moyenne


def bac2literature():
    moyenne = (
        arabe * 4 +
        francais * 3 +
        anglais * 3 +
        philosophie * 3 +
        education_islamique * 2 +
        etudes_sociales * 4 +
        education_physique * 1
    ) / 20
    return moyenne


while True:

    # ÉCOLE PRIMAIRE
    if cycle == "1" or cycle == "école primaire":
        niveau = input(
            "\nÉCOLE PRIMAIRE — Choisissez votre année :\n"
            "1 - Première année du primaire\n"
            "2 - Deuxième année du primaire\n"
            "3 - Troisième année du primaire\n"
            "4 - Quatrième année du primaire\n"
            "5 - Cinquième année du primaire\n"
            "6 - Sixième année du primaire\n"
            "Votre choix : "
        )

        if niveau == "1":
            arabe = float(input("Entrez votre note en arabe (0-10) : "))
            amazighe = float(input("Entrez votre note en amazighe (0-10, si étudiée) : "))
            francais = float(input("Entrez votre note en français (0-10) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-10) : "))
            activites_scientifiques = float(input("Entrez votre note en activités scientifiques (0-10) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-10) : "))
            education_artistique = float(input("Entrez votre note en éducation artistique (0-10) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-10) : "))
            kali = primaryschool123()
            print("Votre moyenne est :", kali)

        elif niveau == "2":
            arabe = float(input("Entrez votre note en arabe (0-10) : "))
            amazighe = float(input("Entrez votre note en amazighe (0-10, si étudiée) : "))
            francais = float(input("Entrez votre note en français (0-10) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-10) : "))
            activites_scientifiques = float(input("Entrez votre note en activités scientifiques (0-10) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-10) : "))
            education_artistique = float(input("Entrez votre note en éducation artistique (0-10) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-10) : "))
            kali = primaryschool123()
            print("Votre moyenne est :", kali)

        elif niveau == "3":
            arabe = float(input("Entrez votre note en arabe (0-10) : "))
            amazighe = float(input("Entrez votre note en amazighe (0-10, si étudiée) : "))
            francais = float(input("Entrez votre note en français (0-10) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-10) : "))
            activites_scientifiques = float(input("Entrez votre note en activités scientifiques (0-10) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-10) : "))
            education_artistique = float(input("Entrez votre note en éducation artistique (0-10) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-10) : "))
            kali = primaryschool123()
            print("Votre moyenne est :", kali)

        elif niveau == "4":
            arabe = float(input("Entrez votre note en arabe (0-10) : "))
            amazighe = float(input("Entrez votre note en amazighe (0-10, si étudiée) : "))
            francais = float(input("Entrez votre note en français (0-10) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-10) : "))
            activites_scientifiques = float(input("Entrez votre note en activités scientifiques (0-10) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-10) : "))
            etudes_sociales = float(input("Entrez votre note en études sociales (0-10) : "))
            education_artistique = float(input("Entrez votre note en éducation artistique (0-10) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-10) : "))
            kali = primaryschool456()
            print("Votre moyenne est :", kali)

        elif niveau == "5":
            arabe = float(input("Entrez votre note en arabe (0-10) : "))
            amazighe = float(input("Entrez votre note en amazighe (0-10, si étudiée) : "))
            francais = float(input("Entrez votre note en français (0-10) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-10) : "))
            activites_scientifiques = float(input("Entrez votre note en activités scientifiques (0-10) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-10) : "))
            etudes_sociales = float(input("Entrez votre note en études sociales (0-10) : "))
            education_artistique = float(input("Entrez votre note en éducation artistique (0-10) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-10) : "))
            kali = primaryschool456()
            print("Votre moyenne est :", kali)

        elif niveau == "6":
            arabe = float(input("Entrez votre note en arabe (0-10) : "))
            amazighe = float(input("Entrez votre note en amazighe (0-10, si étudiée) : "))
            francais = float(input("Entrez votre note en français (0-10) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-10) : "))
            activites_scientifiques = float(input("Entrez votre note en activités scientifiques (0-10) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-10) : "))
            etudes_sociales = float(input("Entrez votre note en études sociales (0-10) : "))
            education_artistique = float(input("Entrez votre note en éducation artistique (0-10) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-10) : "))
            kali = primaryschool456()
            print("Votre moyenne est :", kali)

        else:
            print("Choix d’année invalide.")

        break

    # COLLÈGE
    elif cycle == "2" or cycle == "collège":
        niveau = input(
            "\nCOLLÈGE — Choisissez votre année :\n"
            "1 - Première année du collège\n"
            "2 - Deuxième année du collège\n"
            "3 - Troisième année du collège\n"
            "Votre choix : "
        )

        if niveau == "1":
            arabe = float(input("Entrez votre note en arabe (0-20) : "))
            francais = float(input("Entrez votre note en français (0-20) : "))
            anglais = float(input("Entrez votre note en anglais (0-20) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-20) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-20) : "))
            etudes_sociales = float(input("Entrez votre note en études sociales (0-20) : "))
            sciences_vie_terre = float(input("Entrez votre note en sciences de la vie et de la Terre (0-20) : "))
            physique_chimie = float(input("Entrez votre note en physique-chimie (0-20) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-20) : "))
            kali = middleschool1()
            print("Votre moyenne est :", kali)

        elif niveau == "2":
            arabe = float(input("Entrez votre note en arabe (0-20) : "))
            francais = float(input("Entrez votre note en français (0-20) : "))
            anglais = float(input("Entrez votre note en anglais (0-20) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-20) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-20) : "))
            etudes_sociales = float(input("Entrez votre note en études sociales (0-20) : "))
            sciences_vie_terre = float(input("Entrez votre note en sciences de la vie et de la Terre (0-20) : "))
            physique_chimie = float(input("Entrez votre note en physique-chimie (0-20) : "))
            education_familiale = float(input("Entrez votre note en éducation familiale (0-20) : "))
            informatique = float(input("Entrez votre note en informatique (0-20) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-20) : "))
            kali = middleschool2()
            print("Votre moyenne est :", kali)

        elif niveau == "3":
            arabe = float(input("Entrez votre note en arabe (0-20) : "))
            francais = float(input("Entrez votre note en français (0-20) : "))
            anglais = float(input("Entrez votre note en anglais (0-20) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-20) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-20) : "))
            etudes_sociales = float(input("Entrez votre note en études sociales (0-20) : "))
            sciences_vie_terre = float(input("Entrez votre note en sciences de la vie et de la Terre (0-20) : "))
            physique_chimie = float(input("Entrez votre note en physique-chimie (0-20) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-20) : "))
            kali = middleschool3()
            print("Votre moyenne est :", kali)

        else:
            print("Choix d’année invalide.")

        break

    # LYCÉE
    elif cycle == "3" or cycle == "lycée":
        niveau = input(
            "\nLYCÉE — Choisissez votre niveau :\n"
            "1 - Tronc commun\n"
            "2 - Première année du baccalauréat\n"
            "3 - Deuxième année du baccalauréat\n"
            "Votre choix : "
        )

        if niveau == "1":
            arabe = float(input("Entrez votre note en arabe (0-20) : "))
            francais = float(input("Entrez votre note en français (0-20) : "))
            anglais = float(input("Entrez votre note en anglais (0-20) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-20) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-20) : "))
            etudes_sociales = float(input("Entrez votre note en histoire-géographie (0-20) : "))
            physique_chimie = float(input("Entrez votre note en physique-chimie (0-20) : "))
            sciences_vie_terre = float(input("Entrez votre note en sciences de la vie et de la Terre (0-20) : "))
            philosophie = float(input("Entrez votre note en philosophie (0-20) : "))
            informatique = float(input("Entrez votre note en informatique (0-20) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-20) : "))
            kali=tronc_commun()
            print("Votre moyenne est :", kali)

        elif niveau == "2":
            arabe = float(input("Entrez votre note en arabe (0-20) : "))
            francais = float(input("Entrez votre note en français (0-20) : "))
            anglais = float(input("Entrez votre note en anglais (0-20) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-20) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-20) : "))
            etudes_sociales = float(input("Entrez votre note en histoire-géographie (0-20) : "))
            physique_chimie = float(input("Entrez votre note en physique-chimie (0-20) : "))
            sciences_vie_terre = float(input("Entrez votre note en sciences de la vie et de la Terre (0-20) : "))
            philosophie = float(input("Entrez votre note en philosophie (0-20) : "))
            informatique = float(input("Entrez votre note en informatique (0-20) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-20) : "))
            kali = bac1science()
            print("Votre moyenne est :", kali)

        elif niveau == "3":
            arabe = float(input("Entrez votre note en arabe (0-20) : "))
            francais = float(input("Entrez votre note en français (0-20) : "))
            anglais = float(input("Entrez votre note en anglais (0-20) : "))
            mathematiques = float(input("Entrez votre note en mathématiques (0-20) : "))
            education_islamique = float(input("Entrez votre note en éducation islamique (0-20) : "))
            etudes_sociales = float(input("Entrez votre note en histoire-géographie (0-20) : "))
            physique_chimie = float(input("Entrez votre note en physique-chimie (0-20) : "))
            sciences_vie_terre = float(input("Entrez votre note en sciences de la vie et de la Terre (0-20) : "))
            philosophie = float(input("Entrez votre note en philosophie (0-20) : "))
            informatique = float(input("Entrez votre note en informatique (0-20) : "))
            education_physique = float(input("Entrez votre note en éducation physique (0-20) : "))
            kali = bac2science()
            print("Votre moyenne est :", kali)

        else:
            print("Choix de niveau invalide.")

        break

    else:
        print("\nEntrée invalide. Veuillez relancer le programme et réessayer.")
        break