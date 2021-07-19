from itertools import combinations
def change(x):
    stro = "".join(x)
    for buk in range(0, len(stro)):
        for bukv in range(0, len(stroka)):
            if stro[buk] == stroka[bukv]:
                if ord(stroka[bukv]) % 2 == int(cifr[bukv]) % 2:
                    stro = stro.replace(stro[buk], cifr[bukv])
    return stro
stroka = "AGBOQSTZEL"
cifr = "4680957231"
maxsum = -1
kolvo_nazv = 0
names = list(combinations(stroka, r = 5))
for nazv in range(0, len(names)):
    summa = 0
    kolvo_deL = 0
    nazV = "".join(names[nazv])
    for deL in range(2, ord(nazV[2])):
        if ord(nazV[2]) % deL == 0:
            kolvo_deL += 1
    if kolvo_deL > 6:
        if change(names[nazv]):
            nAzv = change(names[nazv])
            if nAzv[4] != "L":
                    for bukva in range(0, len(nAzv)):
                        if nAzv[bukva] in stroka:
                            summa+=ord(nAzv[bukva])
                        else:
                            summa+=int(nAzv[bukva])
                    if summa % 3 == 0:
                        maxsum = max(maxsum, summa)
                        kolvo_nazv+=1
print(kolvo_nazv, maxsum)
                    
                
        
        
            
            


