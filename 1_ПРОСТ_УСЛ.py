def summa(x):
    summ = 0
    while x > 0:
        summ += x % 10
        x //= 10
    return summ
sum15 = 0
sum21 = 0
min15 = 10**6
min21 = 10**6
for a in range(1001, 20001):
    if summa(a) == 15 and a % 13 == 0:
        min15 = min(min15, a)
        sum15+=1
    elif summa(a) == 21 and a % 17 == 0:
        min21 = min(min21, a)
        sum21+=1
if sum15 == sum21:
    print('1')
elif sum15 > sum21:
    print(min15, sum15)
else:
    print(min21, sum21)
