from a51 import *

cleSecrete = "1100010101111101011000011001010101000101101101000001011011010001"
message = "salut"

initRegistre(cleSecrete)
messageChiffree = chiffrerMessage(message)
print("message", message)
print("coded", messageChiffree)

initRegistre(cleSecrete)
messageDecode = dechifferMessage(messageChiffree)
print("decoded", messageDecode)