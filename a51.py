lsfr1_longueur = 19
lsfr2_longueur = 22
lsfr3_longueur = 23

lsfr1 = 0
lsfr2 = 0
lsfr3 = 0


def xorLSFR1(hasDecalage):
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
    global lsfr2
    b21 = getBitIndice(lsfr2, 21, lsfr2_longueur)

    if hasDecalage:
        b20 = getBitIndice(lsfr2, 20, lsfr2_longueur)

        b = b21 ^ b20
        b = 1 if b else 0

        lsfr2 = decalage(lsfr2, b, lsfr2_longueur)

    return b21


def xorLSFR3(hasDecalage):
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
    return 1 if bLsfr1 + bLsfr2 + bLsfr3 > 1 else 0


def xorGlobal(nb):
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

def initXorRegistres(array):
    firstVal = int(array[0], 2)
    newVals = ""

    for i in range(0, len(array)):
        newVals += str(int(array[i], 2) ^ firstVal)

    return newVals

def initRegistre(key):
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
    binStr = format(binary, 'b').zfill(length)
    binStr += str(toAdd)
    return int(binStr[1:], 2)


def affichageRegistre(registre, longueur):
    print(lsfr1, "=>", format(registre, 'b').zfill(longueur))


def getBitIndice(numberValue, index, longueur):
    return int(format(numberValue, 'b').zfill(longueur)[longueur - (index + 1)])


def getLettreBinaire(lettre):
    return str(''.join(format(ord(el), 'b') for el in lettre))


def getPhraseBinaire(input):
    motConvert = ""
    listBinaires = []

    for lettre in input:
        motConvert += getLettreBinaire(lettre).zfill(8)

    for i in range(0, len(motConvert)):
        listBinaires.append(int(motConvert[i]))

    return listBinaires


def chiffrerMessage(message):
    messageChiffre = ""
    messageBinaire = getPhraseBinaire(message)
    xorResult = xorGlobal(len(messageBinaire))

    for i in range(0, len(messageBinaire)):
        messageChiffre += str(messageBinaire[i] ^ xorResult[i])

    return messageChiffre


def convertirMessageBinaire(messageBinaire):
    messageConvertie = ""

    for i in range(0, len(messageBinaire), 8):
        intValeur = int(messageBinaire[i: i + 8], 2)
        messageConvertie += chr(intValeur)

    return str(messageConvertie)


def dechifferMessage(messageChiffre):
    message = ""
    xorResult = xorGlobal(len(messageChiffre))

    for i in range(0, len(messageChiffre)):
        message += str(int(messageChiffre[i]) ^ xorResult[i])

    return convertirMessageBinaire(str(message))