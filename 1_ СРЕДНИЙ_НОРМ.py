import math
def kolvo(x):
    kol2 = 0
    kol9 = 0
    ch = x
    while x > 0:
        if x % 10 == 2:
            kol2 += 1
        elif x % 10 == 9:
            kol9 += 1
        x //= 10
    if kol2 >= 2 or kol9 >= 2:
        return ch
def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
kolvo_chis = 0
mina = 10**6
minb = 10**6
for a in range(999, 10000):
    kolvo_ispr = 0
    if kolvo(a):
        for pr in range(2, a):
            if a % pr == 0 and is_prime(pr):
                kolvo_ispr += 1
                if kolvo_ispr > 3:
                    kolvo_chis += 1
                    mina = min(mina, a)
                    break
for b in range(11111, 22223):
    kolvo_ispr = 0
    if kolvo(b):
        for pr in range(2, b):
            if b % pr == 0 and is_prime(pr):
                kolvo_ispr += 1
                if kolvo_ispr > 3:
                    kolvo_chis += 1
                    minb = min(minb, b)
                    break
print(kolvo_chis, minb//mina)
