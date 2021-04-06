from a51 import *

# On prend une clé secrète et un message
cleSecrete = "1100010101111101011000011001010101000101101101000001011011010001"
message = "Ici le super test de mon programme"

initRegistre(cleSecrete)
messageChiffree = chiffrerMessage(message)
print("message", message)
print("codé :", messageChiffree)

initRegistre(cleSecrete)
messageDecode = dechifferMessage(messageChiffree)
print("decodé :", messageDecode)
