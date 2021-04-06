lsfr1_longueur = 19
lsfr2_longueur = 22
lsfr3_longueur = 23

lsfr1 = 0
lsfr2 = 0
lsfr3 = 0


def xorLSFR1(hasDecalage):
    """
    Effectue le xor du registre LSFR1
    :param hasDecalage: Indique si le registre doit être décalé
    :return: b n°18
    """
    global lsfr1
    b18 = getBitIndice(lsfr1, 18, lsfr1_longueur)

    if hasDecalage:
        b17 = getBitIndice(lsfr1, 17, lsfr1_longueur)
        b16 = getBitIndice(lsfr1, 16, lsfr1_longueur)
        b13 = getBitIndice(lsfr1, 13, lsfr1_longueur)

        b = b13 ^ b16 ^ b17 ^ b18
        b = 1 if b else 0

        lsfr1 = decalage(lsfr1, b, lsfr1_longueur)

    return b18


def xorLSFR2(hasDecalage):
    """
    Effectue le xor du registre LSFR2
    :param hasDecalage: Indique si le registre doit être décalé
    :return: b n°21
    """
    global lsfr2
    b21 = getBitIndice(lsfr2, 21, lsfr2_longueur)

    if hasDecalage:
        b20 = getBitIndice(lsfr2, 20, lsfr2_longueur)

        b = b21 ^ b20
        b = 1 if b else 0

        lsfr2 = decalage(lsfr2, b, lsfr2_longueur)

    return b21


def xorLSFR3(hasDecalage):
    """
    Effectue le xor du registre LSFR3
    :param hasDecalage: Indique si le registre doit être décalé
    :return: b n°22
    """
    global lsfr3
    b22 = getBitIndice(lsfr3, 22, lsfr3_longueur)

    if hasDecalage:
        b21 = getBitIndice(lsfr3, 21, lsfr3_longueur)
        b20 = getBitIndice(lsfr3, 20, lsfr3_longueur)
        b7 = getBitIndice(lsfr3, 7, lsfr3_longueur)

        b = b7 ^ b20 ^ b21 ^ b22
        b = 1 if b else 0

        lsfr3 = decalage(lsfr3, b, lsfr3_longueur)

    return b22


def getMajoriteBitOrange(bLsfr1, bLsfr2, bLsfr3):
    """
    Renvoie le bit majoritaire à l'emplacement orange des trois registres
    :param bLsfr1: Bit orange LSFR1
    :param bLsfr2: Bit orange LSFR2
    :param bLsfr3: Bit orange LSFR3
    :return: Bit (1 ou 0)
    """
    return 1 if bLsfr1 + bLsfr2 + bLsfr3 > 1 else 0


def xorGlobal(nb):
    """
    Effectue le xor global du système
    :param nb: Nombre de xor à effectuer
    :return: Tableau de bits de résultat des xor
    """
    resBits = []

    for i in range(0, nb):
        bLsfr1 = getBitIndice(lsfr1, 8, lsfr1_longueur)
        bLsfr2 = getBitIndice(lsfr2, 10, lsfr2_longueur)
        bLsfr3 = getBitIndice(lsfr3, 10, lsfr3_longueur)
        majorite = getMajoriteBitOrange(bLsfr1, bLsfr2, bLsfr3)

        b1 = xorLSFR1(bLsfr1 == majorite)
        b2 = xorLSFR2(bLsfr2 == majorite)
        b3 = xorLSFR3(bLsfr3 == majorite)

        res = (1 if b1 else 0) + (1 if b2 else 0) + (1 if b3 else 0) == 1
        b = 1 if res else 0
        resBits.append(b)

    return resBits


def initXorRegistres(key):
    """
    Initialise les registres du système via les xor
    :param key: Clé secrète
    :return: Nouvelle clé secrète
    """
    firstVal = int(key[0], 2)
    newVals = ""

    for i in range(0, len(key)):
        newVals += str(int(key[i], 2) ^ firstVal)

    xorLSFR1(True)
    xorLSFR2(True)
    xorLSFR3(True)

    return newVals


def initRegistre(key):
    """
    Initialise les registres du système
    :param key: Clé secrète
    """
    global lsfr1, lsfr2, lsfr3

    key = initXorRegistres(key)

    debut = 0
    fin = lsfr1_longueur
    lsfr1 = int(key[debut: fin], 2)

    debut += lsfr1_longueur
    fin = debut + lsfr2_longueur
    lsfr2 = int(key[debut: fin], 2)

    debut += lsfr2_longueur
    fin = debut + lsfr3_longueur
    lsfr3 = int(key[debut: fin], 2)


def decalage(binary, toAdd, length):
    """
    Effectue un décalage de registre vers la gauche
    :param binary: Valeur binaire du registre
    :param toAdd: Bit à ajouter à droite
    :param length: Taille du registre
    :return: Nouveau registre
    """
    binStr = format(binary, 'b').zfill(length)
    binStr += str(toAdd)
    return int(binStr[1:], 2)


def afficheRegistre(registre, longueur):
    """
    Affiche un registre
    :param registre: Valeur du registre
    :param longueur: Longueur du registre
    """
    print(lsfr1, "=>", format(registre, 'b').zfill(longueur))


def getBitIndice(numberValue, index, longueur):
    """
    Récupère le bit à l'indice demandé
    :param numberValue: Valeur du registre
    :param index: Indice du bit à récupérer
    :param longueur: Longueur du registre
    :return: Bit à l'indice du registre
    """
    return int(format(numberValue, 'b').zfill(longueur)[longueur - (index + 1)])


def getLettreBinaire(lettre):
    """
    Récupère une lettre binaire
    :param lettre: Lettre
    :return: Valeur de la lettre
    """
    return str(''.join(format(ord(el), 'b') for el in lettre))


def getPhraseBinaire(input):
    """
    Récupère une phrase en binaire
    :param input: Phrase à récupérer
    :return: Tableau contenant chaque valeur de lettre
    """
    motConvert = ""
    listBinaires = []

    for lettre in input:
        motConvert += getLettreBinaire(lettre).zfill(8)

    for i in range(0, len(motConvert)):
        listBinaires.append(int(motConvert[i]))

    return listBinaires


def chiffrerMessage(message):
    """
    Chiffre un message
    :param message: Message à chiffrer
    :return: Message chiffré
    """
    messageChiffre = ""
    messageBinaire = getPhraseBinaire(message)
    xorResult = xorGlobal(len(messageBinaire))

    for i in range(0, len(messageBinaire)):
        messageChiffre += str(messageBinaire[i] ^ xorResult[i])

    return messageChiffre


def convertirMessageBinaire(messageBinaire):
    """
    Converti un message binaire en message lisible
    :param messageBinaire: Message binaire
    :return: Message lisible
    """
    messageConvertie = ""

    for i in range(0, len(messageBinaire), 8):
        intValeur = int(messageBinaire[i: i + 8], 2)
        messageConvertie += chr(intValeur)

    return str(messageConvertie)


def dechifferMessage(messageChiffre):
    """
    Déchiffre un message
    :param messageChiffre: Message chiffré
    :return: Message lisible
    """
    message = ""
    xorResult = xorGlobal(len(messageChiffre))

    for i in range(0, len(messageChiffre)):
        message += str(int(messageChiffre[i]) ^ xorResult[i])

    return convertirMessageBinaire(str(message))
