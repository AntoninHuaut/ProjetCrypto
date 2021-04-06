# TP Cryptographie

> Quentin Fontaine  
> Antonin Huaut

## Fichiers

- a51.py : Contient le code des fonctions de chiffrement à flot A5/1
- diffiehellman.py : Contient le code des fonctions de l'échange de clé Diffie-Hellman
- test_a51.py : Contient du code de test pour le fichier a51.py
- test_diffiehellman.py : Contient du code de test pour les fichiers a51.py et diffiehellman.py

## Problèmes rencontrés

### Initialisation des registres

Nous avons eu du mal à comprendre le fonctionnement de l'initialisation des registres LSFRx.  
Nous pensons avoir corrigé le problème en initialisant les registres avec nos méthodes `initRegistre`
et `initXorRegistres`.

### Problème dans les décalages de registres

Nous avions comme problème que les registres ne se décalaient jamais.  
Après un temps *(qui nous a semblé long)* de recherche, nous avons remarqué que nous avions inversé les conditions de
décalage des fonctions `xorLSFR1`, `xorLSFR2` et `xorLSFR3`.  
Nous utilisions != au lieu de == ...

### Générateur
Enfin, trouver un nombre générateur dans Z/pZ a été compliqué.  
En effet, nous avons un problème de temps de calcul avec notre première méthode. 
Elle fonctionnait sur des nombres p premiers petits mais pas sur un nombre premier de 512bits.  
Nous avons tenté une implémentation qui fait qu'on prend un nombre aléatoire entre 2 et 256 bits (car p = 512 bits) 
et qui vérifie si le pgcd de ce nombre et de p est égal à 1.  
Si c'est le cas, ce nombre est choisi comme générateur.

## Lancer le programme
*(Le programme nécessite Python3 d'installé)*  
Pour lancer le programme de test, tapez la commande :  
`py test_diffiehellman.py` *(En utilisant le Python launcher pour Windows)*  
**OU**  
`python3 test_diffiehellman.py`