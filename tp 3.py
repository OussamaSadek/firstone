import string
import re
f1 = open("myfile.txt", "w")

# fonctions
alphabets = "abcdefghijklmnopqrstuvwxyz"  # this is the english letters


def encrypt(p, k):
    c = ""
    kpos = []  # return the index of characters ex: if k='d' then kpos= 3
    for x in k:
       # kpos += alphabets.find(x) #change the int value to string
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
        if i == len(kpos):
            i = 0
        # find the number or index of the character and perform the shift with the key
        pos = alphabets.find(x) + kpos[i]
        print(pos)
        if pos > 25:
            pos = pos-26               # check you exceed the limit
        # because the cipher text always capital letters
        c += alphabets[pos].capitalize()
        i += 1
    return c


def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
        if i == len(kpos):
            i = 0
        pos = alphabets.find(x.lower()) - kpos[i]
        if pos < 0:
            pos = pos + 26
        p += alphabets[pos].lower()
        i += 1
    return p


dico = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
        13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}


def conversion_en_chiffre(var):
    #  fonction permettant de convertir une lettre en un nombre correspondant dans le dictionnaire
    for x, y in dico.items():
        if var == y:
            return x
    #  renvoye la valeur de x(clé du dic) correspondant a y(valeur du dic)


def conversion_en_lettre(var):
    #  fonction permettant de convertir une nombre en une lettre correspondant dans le dictionnaire
    for x, y in dico.items():
        if var == x:
            return y
    #  renvoye la valeur de y(valeur du dic) correspondant a x(clé du dic)


def pgcd(a, b):
    #  fonction permettant de trouver le pgcd des variables a et b entrés
    nombre = []
    adiviseur = 0
    bdiviseur = 0

    diviseur_aliste = []
    diviseur_bliste = []

    for diviseur in range(1, a+1):
        #  permet de savoir tous les diviseurs de a
        if a % diviseur == 0:
            adiviseur += 1
            diviseur_aliste.append(diviseur)

    for diviseur in range(1, b+1):
        #  permet de savoir tous les diviseurs de b
        if b % diviseur == 0:
            bdiviseur += 1
            diviseur_bliste.append(diviseur)

    for x in diviseur_aliste:
        #  permet de voir le plus grand diviseur commun
        if x in diviseur_bliste:
            nombre.append(x)
            # le dernier index du liste des diviseurs communs <=> pgcd
            pgcdm = len(nombre) - 1

    return nombre[pgcdm]  # renvoie la valeur du pgcd


def verification():
    #  fonction permettant de verifier si le pgcd entre a et 26 est 1
    if acle <= 26:  # le premier parametre doit etre inférieur au second
        pd = pgcd(acle, 26)

        if pd == 1:
            crypter(phrase, acle, bcle)

        else:
            print('Vous devez choisir une autre clé pour eviter des complications')

    elif acle > 26:  # le premier parametre doit etre inférieur au second
        pd = pgcd(26, acle)

        if pd == 1:
            crypter(phrase, acle, bcle)

        else:
            print('Vous devez choisir une autre clé pour eviter des complications')


def crypter(phrase, acle, bcle):
    #  fonction principale permettant de crypter le parametre phrase
    phrase = phrase.lower()  # rendre miniscule tous les caractères

    phrase_chiffre = []
    phrase_crypter = []

    for x in phrase:
        #  changement de tous les caractères en chiffre si existant dans le dictionnaire
        if x not in dico.values():
            phrase_chiffre.append(x)
            #  ne pas changer le caractère au cas où ce n'est pas dans le dictionnaire

        else:
            phrase_chiffre.append(conversion_en_chiffre(x))
            #  fait appel au focntion de conversion ci-dessus pour transformer la lettre en chiffre

    for x in phrase_chiffre:
        if type(x) == type(1):  # si le type est un nombre
            x *= acle  # multiplie le nombre par la clé a
            x += bcle  # additionne le nombre par la clé b
            #  faire l'operation de la transformation affine
            phrase_lettre = conversion_en_lettre(x % 26)
            #  retransformer en lettre le nombre obtenue apres l'operation
            # l'operation se passe en base 26

            phrase_crypter.append(phrase_lettre)
        else:
            phrase_crypter.append(x)
            #  ne pas transformer si c'est pas une lettre
    crypt = ''  # initiation d'une variable de type caractère

    for x in phrase_crypter:
        crypt += x
        #  ajouter dans la variable crypt le resultat

    print(crypt)
    #  afficher la phrase crypter


def decrypter(phrase):
    #  fonction principale permettant de dechiffrer
    phrase = phrase.lower()  # rendre la phrase en miniscule

    phrase_chiffre = []
    phrase_decrypter = []

    for x in phrase:
        #  changement de tous les caractères en chiffre si existant dans le dictionnaire
        if x not in dico.values():
            phrase_chiffre.append(x)
            #  ne pas changer le caractère au cas où ce n'est pas dans le dictionnaire

        else:
            phrase_chiffre.append(conversion_en_chiffre(x))
            #  fait appel au focntion de conversion ci-dessus pour transformer la lettre en chiffre

    for x in phrase_chiffre:

        if type(x) == type(1):  # si le x est un nombre entier
            x -= bcle  # soustrait par la clé b

            while x % acle != 0:  # tant que x n'est pas divisible par la clé a
                x += 26  # ajoute 26 au valeur de x

            #  maintenant x est divisble par a

            x /= acle  # diviser maintenant x par la clé a

            phrase_lettre = conversion_en_lettre(x % 26)
            #  convertir maintenant le nombre en chiffre

            # ajouter dans une liste les caracteres decrypter
            phrase_decrypter.append(phrase_lettre)

        else:  # si le x n'est pas un entier
            # ajouter directement au phrase decrypter (cas des caractères speciaux)
            phrase_decrypter.append(x)

    decrypt = ''  # initialise une variable de type caractère

    for x in phrase_decrypter:
        decrypt += x
        #  ajoute dans le variable decrypt le resultat

    print(decrypt)
    #  affiche le mot  decrypter


algo = input("cesear=1/affine=2/vigenere=3")

alphabets = "abcdefghijklmnopqrstuvwxyz"
choise = input("envrypt=1/decrypt=2: ")
message = input("Enter the message: ")
if algo == "1":
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    choise = input("envrypt=1/decrypt=2: ")
    message = input("Enter the message: ")
    encrypt = ""
    decrypt = ""
    key = 5
    if choise == "1":
        for letter in message:
            new_position = (alphabets.find(letter)*key) % len(alphabets)
            encrypt += alphabets[new_position]
        print("Encrypted message:", encrypt)
    if choise == "2":
        for letter in message:
            new_pos = (alphabets.find(letter)-key) % len(alphabets)
            decrypt += alphabets[new_pos]
        print("Decrypted message:", decrypt)
if algo == "2":

    phrase = input("Entrer le mot a crypter/decrypter:  ")

    acle = int(input('Entrer le valeur de a: '))
    bcle = int(input('Entrer la valeur de b: '))

    choix = int(input(
        ' [0]: Crypter \n [1]: Decrypter \n Veuiller entrer un entier... \n Entrer votre choix: '))
    if choix == 0:
        verification()  # fait appel à la fonction de verification de pgcd
    if choix == 1:
        decrypter(phrase)  # fait appel à la fonction de dechiffrement

if algo == "3":

    print("Welcome to vigenere cipher.\n\n"
          "The text message should contain only characters and the key should be one character word \n"
          "Press 1 to Enrypt a message \npress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
        p = input("enter the plain text: ")
        # this will make sure that there is no space in the message
        p = p.replace(" ", "")
        if p.isalpha():
            k = input("Enter the key: ")
            k = k.strip()  # remove the white spaces from both sides
            if k.isalpha():
               # print(k)
                c = encrypt(p, k)
                print("The cipher text is: ", c)

            else:
                print(k)
                print("Enter valid key, key is only one character word!")
        else:
            print("only letters are allowed !!")

    elif choose == '2':
        c = input("enter the cipher text: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("Enter the key: ")
            if not k.isalpha():
                print("Enter valid key, key is only one character word!")
            else:
                p = decrypt(c, k)
                print("The plain text is: ", p)
        else:
            print("only letters are allowed!")

    else:
        print("Please enter a valid choice!")


f1.close()
