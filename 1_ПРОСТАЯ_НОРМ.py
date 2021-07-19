import math
def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
maxch = -1
kolvo = 0
for a in range(20, 20000):
    sumprost = 0
    for pr in range(2, a):
        if a % pr == 0 and is_prime(pr):
            sumprost += pr
    if sumprost % 2 == a % 2:
        maxch = max(maxch,a)
        kolvo+=1
print(maxch, kolvo)
