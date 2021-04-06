from a51 import *
from diffiehellman import *

# p nombre premier et g générateur dans Z/pZ
p, g = generate_key()

# Alice génère son secret
aliceSecretNb = randint(1, p - 1)
# Et Alice calcule une valeur à partir de son secret
A = square_and_multiply(g, aliceSecretNb, p)

# B génère son secret
bobSecretNb = randint(1, p - 1)
# Et Bob calcule aussi une valeur à partir de son secret
B = square_and_multiply(g, bobSecretNb, p)

# Alice et Bob s'échangent leur valeur A et B

# Alice calcule la clé secrète
secretKey = square_and_multiply(B, aliceSecretNb, p)
# Bob fait de même
secretKeyPrime = square_and_multiply(A, bobSecretNb, p)

# Alice et Bob possède maintenant la même clé secrète
if secretKey != secretKeyPrime:
    raise AssertionError("Le secret est différent")

secretKey = str(bin(secretKey))
a51Key = secretKey[2:66] # On extrait 64 bits après le 0b

# Bob peut maintenant envoyer un message chiffré à Alice, qui sera capable de la déchiffrer

# Initialisation de a51 avec la clé secrète
initRegistre(a51Key)

print("Envoie d'un message par Bob :")
message = "Bonjour Alice, c'est Bob !"
messageChiffree = chiffrerMessage(message)
print("Bob envoie le message :", messageChiffree, " (correspondant à '" + message + "')")

print("\nAlice recoit :", messageChiffree)
# Initialisation de a51 avec la clé secrète du coté de Alice
initRegistre(a51Key)
print("Alice le déchiffre en :", dechifferMessage(messageChiffree))