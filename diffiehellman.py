"""
Des fonctions proviennent du précédant TP effectué au S5 réalisé avec Luc
Certaines fonctions seront peut-être communes entre notre groupe et le groupe de Luc
"""

from random import randint


def euclid(a, b):
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def generateur(n):
    while True:
        k = generate_prime(randint(1, 256), 40)
        if euclid(k, n) == 1:
            return k


# Algorithme d'exponentiation modulaire ET miller-rabin réalisé dans un projet de Math DUT
# On calcule le résultat au fur à mesure grâce à des décalages binaires en regardant le bit de poids faible (via le % 2)
def square_and_multiply(a, k, n):
    n = abs(n)
    p = k
    sumRes = a
    res = 1
    while p >= 1:
        resMod = p % 2

        # Si le bit est à 0, il ne compte pas pour le résultat final
        if resMod == 1:
            res *= sumRes
            res %= n

        p = p // 2
        sumRes = sumRes ** 2 % n

    return res


def miller_rabin(n, d):  # Effectue le test de Miller-Rabin pour k témoins
    # Les cas < 4 sont traités manuellement
    if n == 3:
        return True
    if n - 2 <= 2:
        return False

    for i in range(d):
        a = randint(2, n - 2)
        if temoin(n, a):
            return False  # n est composé
    return True  # n à une probabilité de 4**-k d'être composé


def temoin(n, a):  # Vérifie si l'entier a est un témoin de n
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1
    x = square_and_multiply(a, d, n)
    for i in range(s):
        xi = x ** 2 % n
        if xi == 1 and x != 1 and x != n - 1:
            return True  # a est témoin de n donc n est composé
        x = xi
    if x != 1:
        return True
    return False  # n est probablement premier


# Effectue le test de Miller-Rabin sur des nombres tirés aléatoirement jusqu'à avoir un nombre premier
def generate_prime(k, d):
    puissanceMin = 2 ** (k - 1)
    puissanceMax = 2 ** k
    n = randint(puissanceMin, puissanceMax)
    while n % 2 == 0:
        n = randint(puissanceMin, puissanceMax)
    while not miller_rabin(n, d):
        n = randint(puissanceMin, puissanceMax)
        while n % 2 == 0:
            n = randint(puissanceMin, puissanceMax)
    return n  # nombre premier


def generate_key():
    k = 512
    precision = 40

    _p = generate_prime(k, precision)
    _g = generateur(_p)
    return _p, _g
