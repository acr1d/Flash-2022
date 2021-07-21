from itertools import combinations
def kolvo_cht(x):
    kolvo_nech = 0
    kolvo_ch = 0
    summ = x
    while x > 0:
        if (x % 10) % 2 == 0:
            kolvo_ch += 1
        else:
            kolvo_nech += 1
        x//=10
    if kolvo_nech > kolvo_ch and summ % 2 == 1:
        return summ
    elif kolvo_ch > kolvo_nech and summ % 2 == 0:
        return summ
stroka = "AEIOUY"
x = range(33,127)
sim = list(combinations(x, r = 3))
maxsum = -1
nuzh_l = []
for ch in range(0, len(sim)):
    kolvo_gls = 0
    if kolvo_cht(sum(sim[ch])):
                for buk in sim[ch]:
                        if chr(buk) in stroka or chr(buk) in stroka.lower():
                           kolvo_gls+=1
                if kolvo_gls == 2:
                     if maxsum < sum(sim[ch]):
                         maxsum = sum(sim[ch])
                         print(sim[ch])
                         nuzh_l.append(sim[ch])
for buk in nuzh_l[len(nuzh_l) - 1]:
    if chr(buk) not in stroka and chr(buk) not in stroka.lower():
        print(maxsum ,chr(buk))
