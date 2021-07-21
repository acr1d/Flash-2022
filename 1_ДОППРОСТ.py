kolvo_ch = 0
maxch = -1
for ch in range(100000,200000):
    if ch % 13 == 0 and ((ch % 6 !=0 and ch % 7==0) or (ch % 6 == 0 and ch % 7 != 0)):
        kolvo_ch+=1
        maxch = max(maxch, ch)
        print(ch)
print(kolvo_ch, maxch)
